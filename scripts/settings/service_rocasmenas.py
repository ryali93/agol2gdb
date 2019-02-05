# -*- coding: utf-8 -*-

import os, requests, urllib, urllib2
import shutil, json, uuid
import arcpy
from bs4 import BeautifulSoup

user = 'publicadorapp'
password = 'publ1c4d0r'

# Url de servicios a utilizar
class Services(object):
    def __init__(self):
        self.host = r'https://services1.arcgis.com'
        self.main_url = r'https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_b4f511431ac444cd8d0d3f8245051fc4/FeatureServer/'

        self.GPT_RM_ROCA_MENA           = '0'
        self.TB_RM_01_LITOLOGIA         = '1'
        self.TB_RM_02_MINERALIZACION    = '3'
        self.TB_RM_03_ACTMINERA         = '5'
        self.TB_RM_04_TIPOMUESTRA       = '6'
        self.TB_RM_05_LABORATORIO       = '7'
        self.TB_RM_06_MULTIMEDIA        = '8'

        self.TB_RM_CARACTMIN_ALTER      = '2'
        self.TB_RM_MINERALIZACION_ESTR  = '4'

        self.token = self.getToken()

    # Devuelve el token unico por modulo y maquina
    def getToken(self):
        _URL = "https://www.arcgis.com/sharing/generateToken"
        data = {
            'username': user,
            'password': password,
            'referer': "http://ingemmet-peru.maps.arcgis.com",
            'request': 'gettoken',
            'f': 'json'
        }
        response = requests.post(_URL, data=data)
        response = response.json()
        token = response.get('token', 0)
        return token

    # Url para consulta de codigos de muestra
    @property
    def query_url(self):
        return ''.join([self.main_url, self.GPT_RM_ROCA_MENA, '/query?token={}'.format(self.token)])

    # Url para consulta de fotos
    @property
    def query_url_attach_Photos(self):
        return ''.join([self.main_url, self.TB_RM_06_MULTIMEDIA, '/queryAttachments?token={}'.format(self.token)])

    # Url para la eliminacion de registros
    @property
    def delete_url_GPT_RM_ROCA_MENA(self):
        return ''.join([self.main_url, self.GPT_RM_ROCA_MENA, '/deleteFeatures?token={}'.format(self.token)])

    def __str__(self):
        return self.main_url


# import webbrowser
# poo = Services()
# url = poo.query_url_attach_Photos
# webbrowser.open_new(url)