# -*- coding: utf-8 -*-

from config import *

# Servicios para el modulo de rocas y menas

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
    def name(self):
        res = 'GPT_RM_ROCA_MENA'
        return res

    @property
    def path(self):
        name = self.name
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
    def name(self):
        res = 'TB_RM_01_LITOLOGIA'
        return res

    @property
    def path(self):
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
    def name(self):
        res = 'TB_RM_CARACTMIN_ALTER'
        return res

    @property
    def path(self):
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
    def name(self):
        res = 'TB_RM_MINERALIZACION_ESTR'
        return res

    @property
    def path(self):
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
    def name(self):
        res = 'TB_RM_03_ACTMINERA'
        return res

    @property
    def path(self):
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
        # self.objectid = u'objectid'
        # self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_LB'
        self.ORDEN = u'ORDEN_LB'
        self.TIPO = u'TIPO_A'
        self.ELEMENTO = u'ELEMENTO'
        self.UNIDAD = u'UNIDAD'
        self.SIMBOLO = u'SIMBOLO'
        self.VALOR = u'VALOR'

    @property
    def name(self):
        res = 'TB_RM_05_LABORATORIO'
        return res

    @property
    def path(self):
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
    def name(self):
        res = 'TB_RM_06_MULTIMEDIA'
        return res

    @property
    def path(self):
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

# Servicios para el modulo de geopedologia

class GPT_MS_POG(object):
    def __init__(self):
        self.CODCAL = u'CODCAL'
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.PROY = u'PROY'
        self.PREGLITO = u'PREGLITO'
        self.CODLITO = u'CODLITO'
        self.DATE = u'DATE'
        self.ESPEC = u'ESPEC'
        self.LOCALIDAD = u'LOCALIDAD'
        self.DIST = u'DIST'
        self.PROV = u'PROV'
        self.DEPA = u'DEPA'
        self.HOJA = u'HOJA'
        self.LAT = u'LAT'
        self.LON = u'LON'
        self.Y = u'Y'
        self.X = u'X'
        self.Z = u'Z'
        self.ZONA = u'ZONA'
        self.NMTRACAR = u'NMTRACAR'
        self.NMTRAGEOQ = u'NMTRAGEOQ'
        self.NMTRAROCA = u'NMTRAROCA'
        self.NMTRADUP = u'NMTRADUP'
        self.OBS = u'OBS'
        self.CreationDate = u'CreationDate'
        self.Creator = u'Creator'
        self.EditDate = u'EditDate'
        self.Editor = u'Editor'

    @property
    def name(self):
        res = 'GPT_MS_POG'
        return res

    @property
    def path(self):
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_MS_ECOFISIOGRAFIA(object):
    def __init__(self):
        self.CODCAL = u'CODCAL_ECO'
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CALIDAD = u'CALIDAD'
        self.EDIFIC = u'EDIFIC'
        self.PENDIENTE = u'PENDIENTE'
        self.RELIEVE = u'RELIEVE'
        self.FORMA = u'FORMA'
        self.MICROREL = u'MICROREL'
        self.MATMADRE = u'MATMADRE'
        self.DRENAJE = u'DRENAJE'
        self.PERMEAB = u'PERMEAB'
        self.CONDCLIM = u'CONDCLIM'
        self.VEGETACION = u'VEGETACION'
        self.LITOLOGIA = u'LITOLOGIA'
        self.NAPAFRE = u'NAPAFRE'
        self.PROFENRAIZ = u'PROFENRAIZ'
        self.USO = u'USO'
        self.SUBUSO = u'SUBUSO'
        self.SALES = u'SALES'
        self.SALESESP = u'SALESESP'
        self.FRAGSUP = u'FRAGSUP'
        self.FRAGSUPTAM = u'FRAGSUPTAM'
        self.ERO = u'ERO'
        self.EROSUB = u'EROSUB'
        self.EROGRADO = u'EROGRADO'
        self.ENCOST = u'ENCOST'
        self.ENCCONSIST = u'ENCCONSIST'
        self.GRIETASUP = u'GRIETASUP'
        self.GRIETAPROF = u'GRIETAPROF'
        self.GRIETADIST = u'GRIETADIST'

    @property
    def name(self):
        res = 'TB_MS_ECOFISIOGRAFIA'
        return res

    @property
    def path(self):
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_MS_MORFOPEDOLOGIA(object):
    def __init__(self):
        self.CODCAL = u'CODCAL_MORFO'
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.HRZT = u'HRZT'
        self.HZESP = u'HZESP'
        self.NUMMTRA = u'NUMMTRA'
        self.CODMTRA = u'CODMTRA'
        self.CODMTRAGQ = u'CODMTRAGQ'
        self.CODMTRADUP = u'CODMTRADUP'
        self.HUMEDAD = u'HUMEDAD'
        self.LIMAMP = u'LIMAMP'
        self.LIMFORM = u'LIMFORM'
        self.TEXTURA = u'TEXTURA'
        self.ESTRTIPO = u'ESTRTIPO'
        self.ESTRTAM = u'ESTRTAM'
        self.ESTRGRA = u'ESTRGRA'
        self.COLMATIZ = u'COLMATIZ'
        self.COLVALOR = u'COLVALOR'
        self.COLCROMA = u'COLCROMA'
        self.COLWP = u'COLWP'
        self.CODCOL = u'CODCOL'
        self.CONST = u'CONST'
        self.CONSTSUB = u'CONSTSUB'
        self.CEMENTCONT = u'CEMENTCONT'
        self.CEMENTESTR = u'CEMENTESTR'
        self.CEMENTNAT = u'CEMENTNAT'
        self.CEMENTGRAD = u'CEMENTGRAD'
        self.FRAGRPOR = u'FRAGRPOR'
        self.FRAGRTAM = u'FRAGRTAM'
        self.FRAGRART = u'FRAGRART'
        self.FRAGRFOR = u'FRAGRFOR'
        self.ESTRINTEMP = u'ESTRINTEMP'
        self.MOTABUN = u'MOTABUN'
        self.MOTTAM = u'MOTTAM'
        self.MOTDISTRIB = u'MOTDISTRIB'
        self.MOTMAT = u'MOTMAT'
        self.MOTVAL = u'MOTVAL'
        self.MOTCROM = u'MOTCROM'
        self.MOTWPCOL = u'MOTWPCOL'
        self.MOTCODCOL = u'MOTCODCOL'
        self.MOTNATUR = u'MOTNATUR'
        self.ACTBIOASP = u'ACTBIOASP'
        self.ACTBIOTAM = u'ACTBIOTAM'
        self.ACTBIOCANT = u'ACTBIOCANT'
        self.ABUNBIO = u'ABUNBIO'
        self.TIPOBIO = u'TIPOBIO'
        self.ARTEFHUMAN = u'ARTEFHUMAN'
        self.CON_OTROS = u'CON_OTROS'
        self.REVEST = u'REVEST'
        self.CONCRMIN = u'CONCRMIN'
        self.SUELORG = u'SUELORG'
        self.SUELORGSUB = u'SUELORGSUB'
        self.CARB = u'CARB'
        self.CARBSUB = u'CARBSUB'
        self.YESO = u'YESO'
        self.OLOR = u'OLOR'

    @property
    def name(self):
        res = 'TB_MS_MORFOPEDOLOGIA'
        return res

    @property
    def path(self):
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

class TB_MS_FOTOS(object):
    def __init__(self):
        self.globalid = "globalid"
        self.CODCAL = "CODCAL_FOTOS"
        self.NOMBRE = "NOMBRE"

    @property
    def name(self):
        res = 'TB_MS_FOTOS'
        return res

    @property
    def path(self):
        res = os.path.join(conn, self.name)
        return res

    def __str__(self):
        return self.name

# Servicios para el modulo de fuentes de agua subterranea

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
    def name(self):
        res = 'GPT_DGAR_FA'
        return res

    @property
    def path(self):
        name = self.name
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

    @property
    def name(self):
        res = 'TB_FA_MULTIMEDIA'
        return res

    @property
    def path(self):
        name = self.name
        res = os.path.join(conn, name)
        return res

    def __str__(self):
        return self.name

# Servicios para el modulo de ANAPs

class GPT_DRME_ANAPS(object):
    def __init__(self):
        self.objectid 	= u'objectid'
        self.globalid 	= u'globalid'
        self.PROY = u'PROY'
        self.SUB_PROY = u'SUB_PROY'
        self.CD_MTRA = u'CD_MTRA'
        self.F_MTRA = u'F_MTRA'
        self.GEOLOGO = u'GEOLOGO'
        self.AREA_ESTUDIO = u'AREA_ESTUDIO'
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
        self.COMUNIDAD = u'COMUNIDAD'
        self.PARAJE = u'PARAJE'
        self.CARAC_MUESTRA = u'CARAC_MUESTRA'
        self.TIPO_MUESTRA = u'TIPO_MUESTRA'
        self.TIPO_ANALISIS = u'TIPO_ANALISIS'
        self.LITOLOGIA = u'LITOLOGIA'
        self.ALTERACION = u'ALTERACION'
        self.MINERALIZACION = u'MINERALIZACION'
        self.OTROS = u'OTROS'

    @property
    def name(self):
        res = 'GPT_ANAPS_MUESTREO'
        return res

    @property
    def path(self):
        name = self.name
        res = os.path.join(conn, name)
        return res

    def __str__(self):
        return self.name

class TB_ANAPS_01_LABORATORIO(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_LA'
        self.ORDEN = u'ORDEN_LB'
        self.TIPO = u'TIPO_A'
        self.ELEMENTO = u'ELEMENTO'
        self.UNIDAD = u'UNIDAD'
        self.SIMBOLO = u'SIMBOLO'
        self.VALOR = u'VALOR'

    @property
    def name(self):
        res = 'TB_ANAPS_01_LABORATORIO'
        return res

    @property
    def path(self):
        name = self.name
        res = os.path.join(conn, name)
        return res

    def __str__(self):
        return self.name

class TB_ANAPS_02_MULTIMEDIA(object):
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.CD_MTRA = u'CD_MTRA_MU'
        self.ARCHIVO = u'ARCHIVO'
        self.TITULO = u'TITULO'
        self.FECHA = u'FECHA'
        self.AUTOR = u'AUTOR'
        self.TIPO = u'TIPO_F'
        self.DSCP = u'DSCP'
        self.OBS = u'OBS'
        self.EXT_ARCH = u'EXT_ARCH'
        self.ORDEN = u'ORDEN'
        self.LINK = u'LINK'

    @property
    def name(self):
        res = 'TB_ANAPS_02_MULTIMEDIA'
        return res

    @property
    def path(self):
        name = self.name
        res = os.path.join(conn, name)
        return res

    def __str__(self):
        return self.name
