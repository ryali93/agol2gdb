import requests

_USER = 'publicadorapp'
_PASSWORD = 'publ1c4d0r'

modules = {
    "DGR_GEOPEDOLOGIA": {
        "name": "GPT_MS_POG",
        "alias": "geopedologia",
        "CD_MTRA": "CODCAL",
        "main_url": "https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_1d35578ed5e941a7b6797c257e30c14e/FeatureServer/",
        "tables":
            {
                "0": "GPT_MS_POG",
                "1": "TB_MS_ECOFISIOGRAFIA",
                "2": "TB_MS_MORFOPEDOLOGIA",
                "3": "TB_MS_FOTOS"
            }
    },
    "DRME_ROCASMENAS": {
        "name": "GPT_MS_POG",
        "alias": "geopedologia",
        "CD_MTRA": "CD_MTRA",
        "main_url": "https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_b4f511431ac444cd8d0d3f8245051fc4/FeatureServer/",
        "tables":
            {
                '0': "GPT_RM_ROCA_MENA",
                '1': "TB_RM_01_LITOLOGIA",
                '3': "TB_RM_02_MINERALIZACION",
                '5': "TB_RM_03_ACTMINERA",
                '6': "TB_RM_04_TIPOMUESTRA",
                '7': "TB_RM_05_LABORATORIO",
                '8': "TB_RM_06_MULTIMEDIA",

                '2': "TB_RM_CARACTMIN_ALTER",
                '4': "TB_RM_MINERALIZACION_ESTR"
            }
    },
    "DGAR_FUENTEAGUA_SUB": {
        "name": "GPT_DGAR_FASUB",
        "alias": "geopedologia",
        "CD_MTRA": "CD_MTRA",
        "main_url": "https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_17c106ac35964f64be6708ff48abd974/FeatureServer/",
        "tables":
            {
                "0": "GPT_DGAR_FASUB",
                "3": "TB_FA_MULTIMEDIA"
            }
    }
}

def getToken():
    '''
    :return: Devuelve el token unico por modulo y maquina 
    '''
    _URL = "https://www.arcgis.com/sharing/generateToken"
    data = {
        'username': _USER,
        'password': _PASSWORD,
        'referer': "http://ingemmet-peru.maps.arcgis.com",
        'request': 'gettoken',
        'f': 'json'
    }
    response = requests.post(_URL, data=data)
    response = response.json()
    token = response.get('token', 0)
    return token

token = getToken()

class services(object):
    def __init__(self, module):
        self.main_url = modules[module]["main_url"]
        self.tbs = [x for x in modules[module]["tables"].items()]
        self.tbsId = sorted([x[0] for x in self.tbs])
        self.tbnames = sorted([x[1] for x in self.tbs])
        self.token = getToken()
        self.tbmultimedia = str(max(self.tbsId))

    @property
    def query_url(self):
        return ''.join([self.main_url, str(min(self.tbsId)), '/query?token={}'.format(token)])

    @property
    def query_url_attachs(self):
        return ''.join([self.main_url, str(max(self.tbsId)), '/queryAttachments?token={}'.format(token)])

    @property
    def delete_url(self):
        return ''.join([self.main_url, str(min(self.tbsId)), '/deleteFeatures?token={}'.format(token)])