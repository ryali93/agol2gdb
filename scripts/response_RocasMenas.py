# -*- coding: utf-8 -*-
from settings.model_rocasmenas import *
from settings.nls_ import *

reload(sys)
sys.setdefaultencoding('Windows-1252')
arcpy.env.overwriteOutput = True

class Response_RocasMenas:
    def __init__(self, oid=None):
        self.oid = oid if oid else ''
        self.srv = Services()
        self.scratch = Statics().scratch

        self.GPT_RM     = GPT_RM_ROCA_MENA()
        self.TB_RM_01   = TB_RM_01_LITOLOGIA()
        self.TB_RM_01_1 = TB_RM_CARACTMIN_ALTER()
        self.TB_RM_02   = TB_RM_02_MINERALIZACION()
        self.TB_RM_02_1 = TB_RM_MINERALIZACION_ESTR()
        self.TB_RM_03   = TB_RM_03_ACTMINERA()
        self.TB_RM_04   = TB_RM_04_TIPOMUESTRA()
        self.TB_RM_05   = TB_RM_05_LABORATORIO()
        self.TB_RM_06   = TB_RM_06_MULTIMEDIA()

        self.deleteGPT_RM_ROCA_MENA = self.srv.delete_url_GPT_RM_ROCA_MENA

        self.msg = Messages()
        self.jsonresponse = None
        self.identifiers = None
        self.responseId = None

    def getFields(self, table):
        self.items=[]
        if table == "GPT_RM_ROCA_MENA":
            self.items = self.GPT_RM.__dict__.items()
        elif table == "TB_RM_01_LITOLOGIA":
            self.items = self.TB_RM_01.__dict__.items()
        elif table == "TB_RM_CARACTMIN_ALTER":
            self.items = self.TB_RM_01_1.__dict__.items()
        elif table == "TB_RM_02_MINERALIZACION":
            self.items = self.TB_RM_02.__dict__.items()
        elif table == "TB_RM_MINERALIZACION_ESTR":
            self.items = self.TB_RM_02_1.__dict__.items()
        elif table == "TB_RM_03_ACTMINERA":
            self.items = self.TB_RM_03.__dict__.items()
        elif table == "TB_RM_04_TIPOMUESTRA":
            self.items = self.TB_RM_04.__dict__.items()
        elif table == "TB_RM_05_LABORATORIO":
            self.items = self.TB_RM_05.__dict__.items()
        elif table == "TB_RM_06_MULTIMEDIA":
            self.items = self.TB_RM_06.__dict__.items()
        self.fields = [x[1] for x in self.items]

    def responseRows(self, query):
        response = requests.post(
            query,
            data={
                'where': '1=1',
                'outFields': self.fields,
                'f': 'pjson',
                'token': self.srv.token
            }
        )
        res = json.loads(response.text)
        if res.get('error'):
            arcpy.AddMessage(
                res.get("error").get('message')
            )
        else:
            self.globalids = [[x.get("attributes").get("objectid"), x.get("attributes").get("globalid")] for x in
                              res.get("features")]
            self.jsonresponse = res

    def responseImageGid(self, query):
        response = requests.post(
            query,
            data={
                'where': '1=1',
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

    def datosFotos(self):
        self.listaFotos = []
        for m in self.listaCDMTRA:
            for n in self.listaParGlo:
                if m[0][1:-1].lower() == n[0]:
                    self.listaFotos.append([m[1], n[1]])
        print self.listaFotos

    def responseImagePhotos(self, globalId):
        print globalId
        print self.TB_RM_06.query_url_attach
        response = requests.post(
            self.TB_RM_06.query_url_attach,
            # srv.query_url_attach_Photos,
            data={
                "definitionExpression": "globalid='%s'" % globalId,
                "f": "html",
                'token': self.srv.token
            }
        )
        self.response = response.text
        print response

    def navResponseHTML(self):
        print self.response
        soup = BeautifulSoup(self.response, "lxml")
        self.soup = soup.find("table", {"class": "ftrTable"})

    # def insertImage(self, codmtra, image):
    #     oc = arcpy.da.InsertCursor(self.TB_RM_06.path, [self.TB_RM_06.CD_MTRA, self.TB_RM_06.ARCHIVO])
    #     oc.insertRow([codmtra, image])

    def updateImageTable(self):
        for cd_mtraImage in self.lista_CDMTRA_Image:
            print cd_mtraImage
            arcpy.AddField_management(self.copy, self.TB_RM_06.ARCHIVO, "BLOB")
            sql = "{} = '{}'".format(self.TB_RM_06.CD_MTRA, cd_mtraImage[0])
            with arcpy.da.UpdateCursor(self.copy, [self.TB_RM_06.ARCHIVO], sql) as cursor:
                for x in cursor:
                    x[0] = cd_mtraImage[1]
                    cursor.updateRow(x)
                    print "entra una imagen"

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
            self.listaCDMTRA = [[x[0], x[1]] for x in arcpy.da.SearchCursor(self.copy, ["EVENTID", "CD_MTRA"])]
        if table.split("_")[0] == "TB":
            self.copy = arcpy.TableToTable_conversion(feature, self.scratch, '{}a{:.5}'.format(table, str(uuid.uuid4())))

    def appendData(self, feature, tipodato):
        [arcpy.AlterField_management(self.copy, x[1], x[0]) for x in self.items if x[0] != x[1]]
        if tipodato != "tabla":
            self.updateImageTable()
        print self.copy
        print feature.path
        arcpy.management.Append(self.copy, feature.path, "NO_TEST")

    def deleteRowsService(self, table):
        response = requests.post(
            table,
            data={
                'where': '1=1',
                'f': 'pjson'
            }
        )
        res_tmp = json.loads(response.text)
        res = res_tmp.get('deleteResults')
        if res:
            succes = res[0].get('success')
            if succes:
                arcpy.AddMessage(
                    self.msg.succesdelete.format(self.oid)
                )
            else:
                arcpy.AddError(
                    self.msg.faileddelete.format(self.oid)
                )
                raise
        else:
            arcpy.AddError(
                self.msg.faileddelete.format(self.oid)
            )
            raise

    def processTB(self, table, tipodato="tabla"):
        print table.name
        arcpy.AddMessage(self.msg.initFicha)
        self.getFields(table.name)
        arcpy.AddMessage(self.msg.waitresponse)
        self.responseRows(query=table.query_url)
        if self.jsonresponse.get('features'):
            self.responseToTable(table.name)
            self.appendData(table, tipodato)
        else:
            arcpy.AddMessage(
                self.msg.failedquery
            )

    def processImg(self, table):
        self.responseImageGid(query=table.query_url)  # here
        self.datosFotos()
        self.lista_CDMTRA_Image = []
        for x in self.listaFotos:
            self.responseImagePhotos(globalId=x[1])
            self.navResponseHTML()
            if self.soup:
                self.soup.find_all(href=True)
                url_img = r''.join([self.srv.main_url, self.soup.a['href']])
                filedata = urllib2.urlopen(url_img)
                image = filedata.read()
                self.lista_CDMTRA_Image.append([x[0], image])
                # self.insertImage(x[0], image)

    # en desarrollo
    def deleteAgol(self):
        self.deleteRowsService(self.srv.delete_url_Photos)
        self.deleteRowsService(self.srv.delete_url_fECO)
        self.deleteRowsService(self.srv.delete_url_fMORFO)
        self.deleteRowsService(self.srv.delete_url_fPOG)

    def process(self):
        self.processTB(self.GPT_RM, "tabla")
        # self.processTB(self.TB_RM_01, "tabla")
        # self.processTB(self.TB_RM_01_1, "tabla")
        # self.processTB(self.TB_RM_02, "tabla")
        # self.processTB(self.TB_RM_02_1, "tabla")
        # self.processTB(self.TB_RM_03, "tabla")
        # self.processTB(self.TB_RM_04, "tabla")
        # self.processTB(self.TB_RM_05, "tabla")
        #Imagen
        self.processImg(self.TB_RM_06)
        self.processTB(self.TB_RM_06, "imagen")

    def main(self):
        try:
            self.process()
        except Exception as e:
            arcpy.AddMessage("\n\t" + str(e))
            raise

if __name__ == "__main__":
    poo = Response_RocasMenas()
    poo.main()
