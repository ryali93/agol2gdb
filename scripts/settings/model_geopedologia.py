# -*- coding: utf-8 -*-

from service_geopedologia import *
from static import *

conn = Statics().conn

class FichaPOG:
    def __init__(self):
        self.objectid = u'objectid'
        self.globalid = u'globalid'
        self.PROY = u'PROY'
        self.PREGLITO = u'PREGLITO'
        self.CODLITO = u'CODLITO'
        self.CODCAL = u'CODCAL'
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

class FichaECO:
    def __init__(self):
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
        # self.parentglobalid = u'parentglobalid'
        # self.CreationDate = u'CreationDate'
        # self.Creator = u'Creator'
        # self.EditDate = u'EditDate'
        # self.Editor = u'Editor'

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

class FichaMORFO:
    def __init__(self):
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
        # self.parentglobalid = u'parentglobalid'
        # self.CreationDate = u'CreationDate'
        # self.Creator = u'Creator'
        # self.EditDate = u'EditDate'
        # self.Editor = u'Editor'

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

class FichaFOTO:
    def __init__(self):
        self.globalid = "Globalid"
        self.calicata = "CODCAL"
        self.image = "IMAGE"

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