# -*- coding: utf-8 -*-
from models import *
from messages import *
from services import *
import arcpy, sys, json, uuid
import urllib2
import traceback

reload(sys)
sys.setdefaultencoding('Windows-1252')
arcpy.env.overwriteOutput = True

_SCRATCH = arcpy.env.scratchGDB

def sampleCounting(modulo):
    url = services(modulo).query_url
    response = requests.post(
        url,
        data={
            'where': '1=1',
            'outFields': '*',
            'f': 'pjson',
            'token': token
        }
    )
    res = json.loads(response.text)
    return res.get('features')

def getValuefromCode(clase, nombrecode):
    elm = clase.__dict__.get(nombrecode)
    return elm

class response(object):
    def __init__(self, module=None, cdmtra=None):
        self.cdmtra = "('%s')" % "','".join(cdmtra.split(",")) if cdmtra else None
        self.srv = services(module)
        self.scratch = _SCRATCH

        self.CDMTRA = modules[module]["CD_MTRA"]
        self.FieldArchivoImg = "IMAGE"
        self.estado = "REVISION"

        self.msg = Messages()
        self.jsonresponse = None
        self.identifiers = None
        self.responseId = None

    # Extrae los campos del archivo Model, dependiendo del modulo
    def getFields(self, table):
        self.items = table().__dict__.items()
        self.fields = [x[1] for x in self.items]

    # Request de datos Agol2Gdb
    def responseRows(self, query):
        response = requests.post(
            query,
            data={
                'where': '{}'.format(self.query),
                'outFields': self.fields,
                'f': 'pjson',
                'token': self.srv.token
            }
        )
        res = json.loads(response.text)
        if res.get('error'):
            arcpy.AddMessage(res.get("error").get('message'))
        else:
            self.globalids = [[x.get("attributes").get("objectid"), x.get("attributes").get("globalid")] for x in res.get("features")]
            self.jsonresponse = res

    # Request de GlobalId de tabla de imagenes
    def responseImageGid(self, query):
        response = requests.post(
            query,
            data={
                'where': '{}'.format(self.query),
                'outFields': "parentglobalid, globalid",
                'f': 'pjson',
                'token': self.srv.token
            }
        )
        response = json.loads(response.text)
        lista = []
        for x in response.get("features"):
            for k, v in x.items():
                listatemp = []
                for m, n in v.items():
                    listatemp.append(n)
                lista.append(listatemp)
        self.listaParGlo = lista
        return self.listaParGlo

    # Lista de CDMTRA con fotos
    def datosFotos(self):
        listaFotos = []
        for m in self.listaCDMTRA:
            for n in self.listaParGlo:
                if m[0][1:-1].lower() == n[0]:
                    listaFotos.append([m[1], n[1]])
        return listaFotos

    # Recoge todas las rutas de las imagenes
    def responseAttachments(self):
        response = requests.post(
            self.srv.query_url_attachs,
            data={
                "definitionExpression": "{}".format(self.query),
                "f": "pjson",
                'token': self.srv.token
            }
        )
        res = json.loads(response.text)
        jsonresponse = res.get("attachmentGroups")
        return jsonresponse

    # Actualiza el campo de la imagen para la tabla de multimedia creado
    def updateImageTable(self, row):
        if self.FieldArchivoImg not in [x.name for x in arcpy.ListFields(self.copy)]:
            arcpy.AddField_management(self.copy, self.FieldArchivoImg, "BLOB")
        if "TIPO" not in [x.name for x in arcpy.ListFields(self.copy)]:
            arcpy.AddField_management(self.copy, "TIPO", "TEXT", "30")

        fields = [self.FieldArchivoImg, self.CDMTRA, "TIPO"]

        oc = arcpy.da.InsertCursor(self.copy, fields)
        oc.insertRow([row[0], row[1], row[2]])

    # Actualiza y pule los campos de las imagenes
    def filterImageTable(self):
        listaCDMTRA = list(set([x[0] for x in arcpy.da.SearchCursor(self.copy, self.CDMTRA)]))
        for m in listaCDMTRA:
            sql = "{} = '{}'".format(self.CDMTRA, m)
            titleTmp = ""
            [arcpy.AddField_management(self.copy, campo, "TEXT", "30") for campo in ["NOMBRE", "TIPO"] if campo not in [x.name for x in arcpy.ListFields(self.copy)]]
            with arcpy.da.UpdateCursor(self.copy, ["NOMBRE", "TIPO", self.FieldArchivoImg], sql) as cursor:
                for x in cursor:
                    if x[0] is not None:
                        titleTmp = x[0]
                    if x[0] is None:
                        x[0] = titleTmp
                        cursor.updateRow(x)
                    if x[2] is None:
                        cursor.deleteRow()
                        break
                    if x[1] is None:
                        cursor.deleteRow()

    # Reconoce GPT o TB y crea archivos temporales que almacenaran los datos que seran subidos
    def responseToTable(self, table):
        array = [x.get('attributes') for x in self.jsonresponse.get('features')]
        self.identifiers = [[x.get('globalid'), x.get('objectid')] for x in array]
        self.identifiers.sort(key=lambda x: x[1])

        pth = os.path.join(self.scratch, 'temp')
        feature = arcpy.AsShape(self.jsonresponse, True)
        if table.split("_")[0] == "GPT":
            self.copy = arcpy.CopyFeatures_management(feature, pth)
            arcpy.management.AddField(self.copy, "EVENTID", "GUID")
            n = 0
            with arcpy.da.UpdateCursor(self.copy, ["EVENTID"]) as cursorU:
                for row in cursorU:
                    mmm = self.identifiers[n][0].upper()
                    row[0] = u'{}'.format('{' + mmm + '}')
                    cursorU.updateRow(row)
                    n = n + 1
            del cursorU
            self.listaCDMTRA = [[x[0], x[1]] for x in arcpy.da.SearchCursor(self.copy, ["EVENTID", self.CDMTRA])]
            arcpy.DeleteField_management(self.copy, "globalid")

        if table.split("_")[0] == "TB":
            self.copy = arcpy.TableToTable_conversion(feature, self.scratch, '{}a{:.5}'.format(table, str(uuid.uuid4())))

    # Actualiza campos a ser subidos y los datos temporales (GPT, TB) del Scratch a la BD
    def appendData(self, feature):
        [arcpy.AlterField_management(self.copy, x[1], x[0]) for x in self.items if x[0] != x[1]]
        if "REGISTRO" not in [x.name for x in arcpy.ListFields(self.copy)]:
            arcpy.management.AddField(self.copy, "REGISTRO", "TEXT", "#", "#", 50)
        with arcpy.da.UpdateCursor(self.copy, ["REGISTRO"]) as cursor:
            for x in cursor:
                x[0] = self.estado
                cursor.updateRow(x)
        if self.tipodato == "tabla":
            arcpy.management.Append(self.copy, feature.path, "NO_TEST")

    # Subir los datos temporales (GPT, TB e Image) del Scratch a la BD
    def appendImageTable(self, feature):
        arcpy.management.Append(self.copy, feature.path, "NO_TEST")

    # Eliminar del Agol los datos que ya han pasado a la Base de datos
    def deleteRowsService(self, table):
        query = '1=1' if self.cdmtra is None else "{} IN {}".format(self.CDMTRA, self.cdmtra)
        response = requests.post(
            table,
            data={
                'where': '{}'.format(query),
                'f': 'pjson',
                'token': self.srv.token
            }
        )
        res_tmp = json.loads(response.text)
        res = res_tmp.get('deleteResults')
        if res:
            succes = res[0].get('success')
            if succes:
                arcpy.AddMessage(
                    self.msg.succesdelete.format(self.cdmtra)
                )
            else:
                arcpy.AddError(
                    self.msg.faileddelete.format(self.cdmtra)
                )
                raise
        else:
            arcpy.AddError(
                self.msg.faileddelete.format(self.cdmtra)
            )
            raise

    # Proceso de Tablas
    def processTB(self, table):
        if self.jsonresponse.get('features'):
            self.responseToTable(table.name)
            self.appendData(table)
            arcpy.AddMessage(self.msg.insertdata)
        else:
            arcpy.AddMessage(self.msg.failedquery)

    # Proceso de Imagenes
    def processImg(self, table, query):
        try:
            self.responseImageGid(query=query)  # here
            listaFotos = self.datosFotos()
            jsonImg = self.responseAttachments()
            photos = []
            for m in listaFotos:
                for n in jsonImg:
                    pgid = n.get("parentObjectId")
                    if m[1] == n.get("parentGlobalId"):
                        for j in n.get("attachmentInfos"):
                            photos.append([pgid, j.get("id"), m[0], j.get("keywords")])
            arcpy.AddMessage(self.msg.loadimageaction)
            for x in photos:
                url_img = os.path.join(self.srv.main_url, str(max(self.srv.tbsId)), str(x[0]), "attachments", "{}?token={}".format(x[1], self.srv.token))
                filedata = urllib2.urlopen(url_img)
                image = filedata.read()
                row = [image, x[2], x[3], x[0], x[1]]
                self.updateImageTable(row)
            if len(photos) > 0:
                self.filterImageTable()
                self.appendImageTable(table)
        except Exception:
            traceback.print_exc()
            arcpy.AddMessage(self.msg.runtimeerror)

    # Proceso de eliminar
    def deleteAgol(self):
        try:
            self.deleteRowsService(self.srv.delete_url)
        except:
            pass

    def process(self):
        global i
        self.tipodato = "tabla"
        for tabla in sorted(self.srv.tbs, key=lambda x: x[0]):
            tbid, tb = tabla[0], eval(tabla[1])
            arcpy.AddMessage("\n{}".format(tb().name))

            cdmtraquery = getValuefromCode(tb(), self.CDMTRA)

            self.query = '1=1' if self.cdmtra is None else "{} IN {}".format(cdmtraquery, self.cdmtra)
            query_url = ''.join([self.srv.main_url, str(tbid), '/query'])
            if tbid == self.srv.tbmultimedia:
                self.tipodato = "image"

            arcpy.AddMessage(self.msg.initFicha)
            self.getFields(tb().__class__)
            arcpy.AddMessage(self.msg.waitresponse)
            self.responseRows(query=query_url)
            self.processTB(tb())
            if self.tipodato == "image":
                self.processImg(tb(), query=query_url)

        # Delete
        self.deleteAgol()

    def main(self):
        try:
            self.process()
        except Exception as e:
            arcpy.AddMessage("\n\t" + str(e))
            raise

# if __name__ == "__main__":
#     poo = response("DRME_ROCASMENAS")
#     poo.main()