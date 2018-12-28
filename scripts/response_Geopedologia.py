# -*- coding: utf-8 -*-
import sys
from settings.model_geopedologia import *
from settings.nls import *
import cx_Oracle
import win32com.client
import pandas as pd
import numpy as np
reload(sys)
sys.setdefaultencoding('Windows-1252')


arcpy.env.overwriteOutput = True

def conn():
    inst = "bdgeocat"
    user_sde = "bdtecnica"
    password_sde = "bdtecnica"
    connect = cx_Oracle.connect(user_sde, password_sde, inst)
    return connect

conexion = conn()

class ResponseGeopedologia:
    def __init__(self, oid=None):
        self.oid = oid if oid else ''
        self.srv = Services()
        self.scratch = Statics().scratch

        self.featPOG = FichaPOG()
        self.featECO = FichaECO()
        self.featMORFO = FichaMORFO()
        self.featFOTO = FichaFOTO()

        self.deletePOG = self.srv.delete_url_fPOG
        self.deleteECO = self.srv.delete_url_fECO
        self.deleteMORFO = self.srv.delete_url_fMORFO
        self.deleteFOTO = self.srv.delete_url_Photos

        self.msg = Messages()
        self.jsonresponse = None
        self.identifiers = None
        self.responseId = None

    def send_email(self, listacod, listaerror):
        listacod2 = [x[1] for x in listacod]
        listacod2.sort()
        listacod2 = '\n'.join(listacod2)
        o = win32com.client.Dispatch("Outlook.Application")
        Msg = o.CreateItem(0)
        # Msg.From = u"comunicacion2@ingemmet.gob.pe"
        # hcastro@ingemmet.gob.pe; jsalcedo@ingemmet.gob.pe;
        Msg.To = u"autonomoosi02@ingemmet.gob.pe"
        # Msg.To = u"autonomodgr03@ingemmet.gob.pe; autonomoosi02@ingemmet.gob.pe"
        Msg.Subject = u"Actualizacion del registro: Módulo de Geopedologia"
        listaerror2 = listaerror
        if len(listaerror2) > 0:
            listaerror2.sort()
            listaerror2 = '\n'.join(listaerror2)
            Msg.Body = u"Los siguientes registros han sido subidos: \n{} \nLos siguientes registros tienen algún error, favor de verificar: \n {} \n Saludos.".format(listacod2, listaerror2)
        else:
            Msg.Body = u"Los siguientes registros han sido subidos: \n{} \n\nSaludos.".format(listacod2)
        Msg.Send()

    def updateRowsPost(self, conn, listaCodcal):
        cursor = conn.cursor()
        expresion_sql = "PKG_SISTEMA_MORFOPEDOLOGIA.P_MS_UPDATEPOG"
        listaerror = []
        for codcal in listaCodcal:
            try:
                cursor.callproc(expresion_sql, [codcal[1]])
            except Exception as e:
                listaerror.append(codcal[1])
        cursor.close()

        self.send_email(listacod=listaCodcal, listaerror=listaerror)

    def updateRowsPrev(self, table):
        utm = {17: 32717, 18: 32718, 19: 32719}
        coordSysWGS = arcpy.SpatialReference(4326)
        for i in utm.items():
            coordSys = arcpy.SpatialReference(i[1])
            tb_i = arcpy.MakeFeatureLayer_management(table, "in_memory\\tb_{}".format(i[0]), "ZONA = '{}'".format(i[0]))
            with arcpy.da.UpdateCursor(tb_i, ["X", "Y", "SHAPE@X", "SHAPE@Y"], None, coordSys) as cursor:
                for x in cursor:
                    x[2] = x[0]
                    x[3] = x[1]
                    cursor.updateRow(x)

            with arcpy.da.UpdateCursor(tb_i, ["LON", "LAT", "SHAPE@X", "SHAPE@Y"], None, coordSysWGS) as cursor:
                for x in cursor:
                    x[0] = x[2]
                    x[1] = x[3]
                    cursor.updateRow(x)

    def getFields(self, table):
        if table == "GPT_MS_POG":
            self.fields = self.featPOG.__dict__.values()
        elif table == "TB_MS_ECOFISIOGRAFIA":
            self.fields = self.featECO.__dict__.values()
        elif table == "TB_MS_MORFOPEDOLOGIA":
            self.fields = self.featMORFO.__dict__.values()

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

    def responseImageGid(self):
        response = requests.post(
            self.srv.query_url_data_Photos,
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
        for m in self.listacodcal:
            for n in self.listaParGlo:
                if m[0][1:-1].lower() == n[0]:
                    self.listaFotos.append([m[1], n[1]])

    def responseImagePhotos(self, globalId):
        response = requests.post(
            self.srv.query_url_attach_Photos,
            data={
                "definitionExpression": "globalid='%s'" % globalId,
                "f": "html",
                'token': self.srv.token
            }
        )
        self.response = response.text

    def navResponseHTML(self):
        soup = BeautifulSoup(self.response, "lxml")
        self.soup = soup.find("table", {"class": "ftrTable"})

    def insertImage(self, codcal, image):
        oc = arcpy.da.InsertCursor(self.featFOTO.path, [self.featFOTO.calicata, self.featFOTO.image])
        oc.insertRow([codcal, image])

    def uploadImage(self):
        self.responseImageGid()
        self.datosFotos()
        for x in self.listaFotos:
            self.responseImagePhotos(globalId=x[1])
            self.navResponseHTML()

            if self.soup:
                self.soup.find_all(href=True)
                url_img = r''.join([self.srv.main_url, self.soup.a['href']])
                filedata = urllib2.urlopen(url_img)
                image = filedata.read()
                self.insertImage(x[0], image)

    def responseIds(self, query):
        ids = requests.post(query,
                            data={
                                'where': '1=1',
                                'outFields': "objectid, globalid, parentglobalid",
                                'f': 'pjson',
                                'token': self.srv.token
                            }
                            )
        ids = json.loads(ids.text)

        lista = []
        for x in ids.get("features"):
            for k, v in x.items():
                listatemp = []
                for m, n in v.items():
                    listatemp.append(n)
                lista.append(listatemp)

        self.ids = lista

    def responseToTable(self, table):
        array = [x.get('attributes') for x in self.jsonresponse.get('features')]
        self.identifiers = [[x.get('globalid'), x.get('objectid')] for x in array]
        self.identifiers.sort(key=lambda x: x[1])
        pth = os.path.join(self.scratch, 'temp')
        feature = arcpy.AsShape(self.jsonresponse, True)

        if table == "GPT_MS_POG":
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
            self.listacodcal = [[x[0], x[1]] for x in arcpy.da.SearchCursor(self.copy, ["EVENTID", "CODCAL"])]
            arcpy.AlterField_management(self.copy, "DATE", "DATE_", "Fecha", "DATE")

        if table != "GPT_MS_POG":
            self.copy = arcpy.TableToTable_conversion(feature, self.scratch, 'a{:.5}'.format(str(uuid.uuid4())))
            arcpy.management.AddField(self.copy, "EVENTID", "GUID")
            arcpy.management.AddField(self.copy, "PARENTGLOBALID", "GUID")
            if "CODCAL" not in [x.name for x in arcpy.ListFields(self.copy)]:
                arcpy.management.AddField(self.copy, "CODCAL", "TEXT", "", "", 15)
            if "CODMTRA" not in [x.name for x in arcpy.ListFields(self.copy)]:
                arcpy.management.AddField(self.copy, "CODMTRA", "TEXT", "", "", 15)
            if "CODMTRAGQ" not in [x.name for x in arcpy.ListFields(self.copy)]:
                arcpy.management.AddField(self.copy, "CODMTRAGQ", "TEXT", "", "", 15)

            n = 0
            with arcpy.da.UpdateCursor(self.copy, ["EVENTID"]) as cursorU:
                for row in cursorU:
                    mmm = self.identifiers[n][0].upper()
                    row[0] = u'{}'.format('{' + mmm + '}')
                    cursorU.updateRow(row)
                    n = n + 1
            del cursorU

            with arcpy.da.UpdateCursor(self.copy, ["EVENTID", "PARENTGLOBALID", "CODCAL"]) as cursorT:
                for row in cursorT:
                    for id in self.ids:
                        if row[0][1:-1] == id[1].upper():
                            row[1] = u'{}'.format('{' + id[0].upper() + '}')
                            for ccal in self.listacodcal:
                                if row[1] == ccal[0]:
                                    row[2] = ccal[1]
                    cursorT.updateRow(row)
            del cursorT

            if table == "TB_MS_MORFOPEDOLOGIA":
                with arcpy.da.UpdateCursor(self.copy, ["CODCAL", "CODMTRA", "CODMTRAGQ"]) as cursorP:
                    for x in cursorP:
                        nmtra = x[1][-1]
                        x[1] = x[0] + "-" + nmtra
                        if x[2] != None:
                            nmtragq = x[2][-1]
                            x[2] = x[0] + "-" + nmtragq
                        cursorP.updateRow(x)
                del cursorP

    def appendData(self, feature, table):
        # Actualizacion para llenar campos
        if table.split('\\')[-1] == "GPT_MS_POG":
            arcpy.management.Append(
                self.copy, feature.path, "NO_TEST"
            )
        elif table.split('\\')[-1] == "TB_MS_ECOFISIOGRAFIA":
            arcpy.management.Append(
                self.copy, feature.path, "NO_TEST"
            )
        elif table.split('\\')[-1] == "TB_MS_MORFOPEDOLOGIA":
            arcpy.management.Append(
                self.copy, feature.path, "NO_TEST"
            )

    def deleteRowsService(self, delete):
        response = requests.post(
            delete,
            data={
                # 'objectIds': self.oid,
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

    def processPOG(self):
        arcpy.AddMessage(self.msg.initFichaPOG)
        self.getFields(FichaPOG().name)
        arcpy.AddMessage(self.msg.waitresponse)
        self.responseRows(query=self.srv.query_url_fPOG)
        if self.jsonresponse.get('features'):
            self.responseToTable("GPT_MS_POG")
            # Fotos
            arcpy.AddMessage(self.msg.loadimageaction)
            self.uploadImage()
            arcpy.AddMessage(self.msg.updateRows)
            self.updateRowsPrev(table=self.copy)
            arcpy.AddMessage(self.msg.insertdata)
            self.appendData(feature=FichaPOG(), table="GPT_MS_POG")
            self.updateRowsPost(conexion, self.listacodcal)
        else:
            arcpy.AddMessage(
                self.msg.failedquery
            )

    def processECO(self):
        # Ficha ECO
        arcpy.AddMessage(self.msg.initFichaECO)
        self.getFields(FichaECO().name)
        arcpy.AddMessage(self.msg.waitresponse)
        self.responseRows(query=self.srv.query_url_fECO)
        self.responseIds(query=self.srv.query_url_fECO)
        if self.jsonresponse.get('features'):
            self.responseToTable("TB_MS_ECOFISIOGRAFIA")
            arcpy.AddMessage(self.msg.insertdata)
            self.appendData(feature=FichaECO(), table="TB_MS_ECOFISIOGRAFIA")
        else:
            arcpy.AddMessage(
                self.msg.failedquery
            )

    def processMORFO(self):
        arcpy.AddMessage(self.msg.initFichaMORFO)
        self.getFields(FichaMORFO().name)
        arcpy.AddMessage(self.msg.waitresponse)
        self.responseRows(query=self.srv.query_url_fMORFO)
        self.responseIds(query=self.srv.query_url_fMORFO)
        if self.jsonresponse.get('features'):
            self.responseToTable("TB_MS_MORFOPEDOLOGIA")
            arcpy.AddMessage(self.msg.insertdata)
            self.appendData(feature=FichaMORFO(), table="TB_MS_MORFOPEDOLOGIA")
        else:
            arcpy.AddMessage(
                self.msg.failedquery
            )

    def deleteAgol(self):
        self.deleteRowsService(self.srv.delete_url_Photos)
        self.deleteRowsService(self.srv.delete_url_fECO)
        self.deleteRowsService(self.srv.delete_url_fMORFO)
        self.deleteRowsService(self.srv.delete_url_fPOG)

    def process(self):
        self.processPOG()
        self.processECO()
        self.processMORFO()

    def main(self):
        try:
            self.process()
        except Exception as e:
            arcpy.AddMessage("\n\t" + str(e))
            raise

if __name__ == "__main__":
    poo = ResponseGeopedologia()
    poo.main()
