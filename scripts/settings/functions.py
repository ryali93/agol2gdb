# -*- coding: utf-8 -*-
import win32com.client

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
        Msg.Body = u"Los siguientes registros han sido subidos: \n{} \nLos siguientes registros tienen algún error, favor de verificar: \n {} \n Saludos.".format(
            listacod2, listaerror2)
    else:
        Msg.Body = u"Los siguientes registros han sido subidos: \n{} \n\nSaludos.".format(listacod2)
    Msg.Send()