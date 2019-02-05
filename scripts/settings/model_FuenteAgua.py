# -*- coding: utf-8 -*-

import sys
from static import *
from service_FuenteAgua import *

static = Statics()
conn = static.conn
srv = Services()

class GPT_DGAR_FASUB(object):
    def __init__(self):
        self.objectid 	= u'objectid'
        self.globalid 	= u'globalid'
        self.CD_PROY 	= u'CD_PROY'
        self.SUB_PROY 	= u'SUB_PROY'
        self.VERTIENTE 	= u'VERTIENTE'
        self.CUENCA 	= u'CUENCA'
        self.SUB_CUEN 	= u'SUB_CUEN'
        self.CD_SUBCUEN = u'CD_SUBCUEN'
        self.MIC_CUEN 	= u'MIC_CUEN'
        self.CD_MICCUEN = u'CD_MICCUEN'
        self.TIPO_CUEN 	= u'TIPO_CUEN'
        self.FORM_CUEN 	= u'FORM_CUEN'
        self.ASP_NATUR 	= u'ASP_NATUR'
        self.NOM_FTE 	= u'NOM_FTE'
        self.CD_MTRA 	= u'CD_MTRA'
        self.DATE_MTRA 	= u'DATE_MTRA'
        self.COLECTADO 	= u'COLECTADO'
        self.USUARIO 	= u'USUARIO'
        self.MONITOREO 	= u'MONITOREO'
        self.FTE_CERT 	= u'FTE_CERT'
        self.QAQC 		= u'QAQC'
        self.QAQC_OBS 	= u'QAQC_OBS'
        self.LATITUD 	= u'LATITUD'
        self.LONGITUD 	= u'LONGITUD'
        self.NORTE 		= u'NORTE'
        self.ESTE 		= u'ESTE'
        self.PRECIS 	= u'PRECIS'
        self.ZONA 		= u'ZONA'
        self.DATUM 		= u'DATUM'
        self.ALTITUD 	= u'ALTITUD'
        self.UBICACION 	= u'UBICACION'
        self.REGION 	= u'REGION'
        self.PROVINCIA 	= u'PROVINCIA'
        self.DISTRITO 	= u'DISTRITO'
        self.HOJA 		= u'HOJA'
        self.FUENTE 	= u'FUENTE'
        self.AGUA_SUB 	= u'AGUA_SUB'
        self.AGUA_SUP 	= u'AGUA_SUP'
        self.NIV_PZM 	= u'NIV_PZM'
        self.PARAM 		= u'PARAM'
        self.ANALISIS 	= u'ANALISIS'
        self.COLOR 		= u'COLOR'
        self.OLOR 		= u'OLOR'
        self.TURBIDEZ 	= u'TURBIDEZ'
        self.ALCALIN 	= u'ALCALIN'
        self.SULFATO 	= u'SULFATO'
        self.NITRATO 	= u'NITRATO'
        self.PRECIPIT 	= u'PRECIPIT'
        self.OC_QAQC 	= u'OC_QAQC'
        self.T_ROCA 	= u'T_ROCA'
        self.ST_ROCA 	= u'ST_ROCA'
        self.DESC_LITO 	= u'DESC_LITO'
        self.AMBGEO_OBS = u'AMBGEO_OBS'
        self.GEOMORFO 	= u'GEOMORFO'
        self.PENDIENTE 	= u'PENDIENTE'
        self.GRAD_FRACT = u'GRAD_FRACT'
        self.RUMBO 		= u'RUMBO'
        self.BUZAM 		= u'BUZAM'
        self.D_BUZAM 	= u'D_BUZAM'
        self.SUELO 		= u'SUELO'
        self.CAUDAL 	= u'CAUDAL'
        self.USO 		= u'USO'
        self.USO_OBS 	= u'USO_OBS'
        self.TEMP_FTE 	= u'TEMP_FTE'
        self.TEMP_AMB 	= u'TEMP_AMB'
        self.PH 		= u'PH'
        self.PH_U 		= u'PH_U'
        self.ORP 		= u'ORP'
        self.U_CE 		= u'U_CE'
        self.CE 		= u'CE'
        self.CE_2 		= u'CE_2'
        self.U_TDS 		= u'U_TDS'
        self.TDS 		= u'TDS'
        self.TDS_2 		= u'TDS_2'
        self.U_SAL 		= u'U_SAL'
        self.SAL 		= u'SAL'
        self.SAL_2 		= u'SAL_2'
        self.U_RESIS 	= u'U_RESIS'
        self.RESIS 		= u'RESIS'
        self.RESIS_2 	= u'RESIS_2'
        self.O_DIS 		= u'O_DIS'
        self.O_DIS_2 	= u'O_DIS_2'
        self.CAPTADO 	= u'CAPTADO'
        self.SABOR 		= u'SABOR'
        self.PROPIEDAD 	= u'PROPIEDAD'
        self.POSTCAMPO 	= u'POSTCAMPO'
        self.CreationDate = u'CreationDate'
        self.Creator = u'Creator'
        self.EditDate = u'EditDate'
        self.Editor = u'Editor'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.GPT_DGAR_FASUB, '/query'])

    @property
    def name(self):
        res = 'GPT_DGAR_FASUB'
        return res

    @property
    def path(self):
        ds = static.ds
        name = ds + "." + self.name
        res = os.path.join(conn, name)
        return res

    def __str__(self):
        return self.name

class TB_FA_MULTIMEDIA(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_MT'
        self.GRAF_UBI = u'GRAF_UBI'
        self.TIPOGRAF = u'TIPOGRAF'
        self.OBS_FTE = u'OBS_FTE'
        self.TITULO = u'TITULO'
        self.FECHA = u'FECHA_M'
        self.AUTOR = u'AUTOR'
        self.TIPO = u'TIPO_M'
        self.DESCRIP = u'DESCRIP'
        self.OBS = u'OBS'
        self.EXT_ARCH = u'EXT_ARCH'
        self.ORDEN = u'ORDEN'
        # self.PARENTGLOBALID = u'parentglobalid'

        # self.ARCHIVO = u'ARCHIVO'
        # self.CROQ1 = u'CROQ1'
        # self.CROQ2 = u'CROQ2'
        # self.CTE_GEOL1 = u'CTE_GEOL1'
        # self.CTE_GEOL2 = u'CTE_GEOL2'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_FA_MULTIMEDIA, '/query'])

    @property
    def query_url_attach(self):
        return ''.join([srv.main_url, srv.TB_FA_MULTIMEDIA, '/queryAttachments'])

    @property
    def name(self):
        res = 'TB_FA_MULTIMEDIA'
        return res

    @property
    def path(self):
        ds = static.ds
        name = ds + "." + self.name
        res = os.path.join(conn, name)
        return res

    def __str__(self):
        return self.name
