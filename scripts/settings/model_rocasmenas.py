# -*- coding: utf-8 -*-

import sys
from static import *
from service_rocasmenas import *

static = Statics()
conn = static.conn
srv = Services()

class GPT_RM_ROCA_MENA(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.PROY = u'PROY'
        self.SUB_PROY = u'SUB_PROY'
        self.CD_MTRA= u'CD_MTRA'
        self.F_MTRA = u'F_MTRA'
        self.COLECTADO = u'COLECTADO'
        self.CAT = u'CAT'
        self.OTR_CAT = u'OTR_CAT'
        self.EST_MIN = u'EST_MIN'
        self.A_ITS = u'A_ITS'
        self.REGISTRO = u'REGISTRO'
        self.F_REGISTRO = u'F_REGISTRO'
        self.REGISTRADO = u'REGISTRADO'
        self.F_CAMBIO = u'F_CAMBIO'
        self.CAMBIADO = u'CAMBIADO'
        self.LATITUD = u'LATITUD'
        self.LONGITUD = u'LONGITUD'
        self.ESTE = u'ESTE'
        self.NORTE = u'NORTE'
        self.DATUM = u'DATUM'
        self.ZONA = u'ZONA'
        self.ALTITUD = u'ALTITUD'
        self.REGION = u'REGION'
        self.PROVINCIA = u'PROVINCIA'
        self.DISTRITO = u'DISTRITO'
        self.HOJA = u'HOJA'
        self.T_YACIMIENTO = u'T_YACIMIENTO'
        self.ST_YACIMIENTO = u'ST_YACIMIENTO'
        self.CreationDate = u'CreationDate'
        self.Creator = u'Creator'
        self.EditDate = u'EditDate'
        self.Editor = u'Editor'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.GPT_RM_ROCA_MENA, '/query'])

    @property
    def name(self):
        res = 'GPT_RM_ROCA_MENA'
        return res

    @property
    def path(self):
        ds = static.ds
        name = ds + "." + self.name
        res = os.path.join(conn, name)
        return res

    def __str__(self):
        return self.name

class TB_RM_01_LITOLOGIA(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_LT'
        self.T_ROCA = u'T_ROCA'
        self.ST_ROCA = u'ST_ROCA'
        self.ROCA_MINERAL = u'ROCA_MINERAL'
        self.GEOMETRIA = u'GEOMETRIA'
        self.TEXTURA = u'TEXTURA'
        self.U_LITOESTRAT = u'U_LITOESTRAT'
        self.DEPOSITO = u'DEPOSITO'
        self.ST_DEPOSITO = u'ST_DEPOSITO'
        self.MENA = u'MENA'
        self.GANGA = u'GANGA'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_01_LITOLOGIA, '/query'])

    @property
    def name(self):
        res = 'TB_RM_01_LITOLOGIA'
        return res

    @property
    def path(self):
        # ds = static.ds
        # name = ds + "." + self.name
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_RM_CARACTMIN_ALTER(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_CALT'
        self.ALTERACION = u'ALTERACION'
        self.INTENSIDAD = u'INTENSIDAD'
        self.GRUPO_ALTR = u'GRUPO_ALTR'
        self.MINERAL = u'MINERAL'
        self.E_ALTERACION = u'E_ALTERACION'
        self.ORDEN = u'ORDEN1'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_CARACTMIN_ALTER, '/query'])

    @property
    def name(self):
        res = 'TB_RM_CARACTMIN_ALTER'
        return res

    @property
    def path(self):
        # ds = static.ds
        # name = ds + "." + self.name
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_RM_02_MINERALIZACION(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_MR'
        self.CONTENIDO_MIN = u'CONTENIDO_MIN'
        self.MINMENA = u'MINMENA'
        self.MINGANGA = u'MINGANGA'
        self.ESTILO_MIN = u'ESTILO_MIN'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_02_MINERALIZACION, '/query'])

    @property
    def name(self):
        res = 'TB_RM_02_MINERALIZACION'
        return res

    @property
    def path(self):
        # ds = static.ds
        # name = ds + "." + self.name
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_RM_MINERALIZACION_ESTR(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_MRE'
        self.ORDEN_ESTR = u'ORDEN_ESTR'
        self.TIPO = u'TIPO'
        self.SUBTIPO = u'SUBTIPO'
        self.AZIMUT = u'AZIMUT'
        self.RUMBO = u'RUMBO'
        self.D_RUMBO = u'D_RUMBO'
        self.BUZAMIENTO = u'BUZAMIENTO'
        self.D_BUZAMIENTO = u'D_BUZAMIENTO'
        self.PLUNGE = u'PLUNGE'
        self.D_PLUNGE = u'D_PLUNGE'
        self.PITCH = u'PITCH'
        self.D_PITCH = u'D_PITCH'
        self.OBSERVACION = u'OBSERVACION'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_MINERALIZACION_ESTR, '/query'])

    @property
    def name(self):
        res = 'TB_RM_MINERALIZACION_ESTR'
        return res

    @property
    def path(self):
        # ds = static.ds
        # name = ds + "." + self.name
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_RM_03_ACTMINERA(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_AM'
        self.ACT_PRD = u'ACT_PRD'
        self.ACT_SC_PRD = u'ACT_SC_PRD'
        self.ACT_RR_RSV = u'ACT_RR_RSV'
        self.ACT_DATO = u'ACT_DATO'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_03_ACTMINERA, '/query'])

    @property
    def name(self):
        res = 'TB_RM_03_ACTMINERA'
        return res

    @property
    def path(self):
        # ds = static.ds
        # name = ds + "." + self.name
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_RM_04_TIPOMUESTRA(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_TM'
        self.T_MTRA = u'T_MTRA'
        self.OTR_MTRA = u'OTR_MTRA'
        self.DSCP_MTRA = u'DSCP_MTRA'
        self.T_MTRO = u'T_MTRO'
        self.OTR_MTRO = u'OTR_MTRO'
        self.DSCP_MTRO = u'DSCP_MTRO'
        self.ANA_GEOQ = u'ANA_GEOQ'
        self.ANA_PETRO = u'ANA_PETRO'
        self.ANA_OTROS = u'ANA_OTROS'
        self.ANA_EESP = u'ANA_EESP'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_04_TIPOMUESTRA, '/query'])

    @property
    def name(self):
        res = 'TB_RM_04_TIPOMUESTRA'
        return res

    @property
    def path(self):
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_RM_05_LABORATORIO(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_LB'
        self.ORDEN = u'ORDEN_LB'
        self.TIPO_A = u'TIPO_A'
        self.ELEMENTO = u'ELEMENTO'
        self.UNIDAD = u'UNIDAD'
        self.SIMBOLO = u'SIMBOLO'
        self.VALOR = u'VALOR'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_05_LABORATORIO, '/query'])

    @property
    def name(self):
        res = 'TB_RM_05_LABORATORIO'
        return res

    @property
    def path(self):
        # ds = static.ds
        # name = ds + "." + self.name
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_RM_06_MULTIMEDIA(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_MU'
        self.TITULO = u'TITULO'
        self.FECHA = u'FECHA'
        self.AUTOR = u'AUTOR'
        self.TIPO = u'TIPO_F'
        self.DSCP = u'DSCP'
        self.OBS = u'OBS'
        self.EXT_ARCH = u'EXT_ARCH'
        self.ORDEN = u'ORDEN'
        self.LINK = u'LINK'
        # self.ARCHIVO = u'ARCHIVO'

    @property
    def query_url(self):
        return ''.join([srv.main_url, srv.TB_RM_06_MULTIMEDIA, '/query'])

    @property
    def query_url_attach(self):
        return ''.join([srv.main_url, srv.TB_RM_06_MULTIMEDIA, '/queryAttachments'])

    @property
    def name(self):
        res = 'TB_RM_06_MULTIMEDIA'
        return res

    @property
    def path(self):
        # ds = static.ds
        # name = ds + "." + self.name
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name
