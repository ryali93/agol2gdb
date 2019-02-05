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
        self.main_url = r'https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_1d35578ed5e941a7b6797c257e30c14e/FeatureServer/'

        self.GPT_MS_POG = "0"
        self.TB_MS_ECO = "1"
        self.TB_MS_MORFO = "2"
        self.TB_MS_FOTO = "3"

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
        return ''.join([self.main_url, self.GPT_MS_POG, '/query?token={}'.format(self.token)])

    # Url para la consulta de imagenes (Photos)
    @property
    def query_url_attach_Photos(self):
        return ''.join([self.main_url, self.TB_MS_FOTO, '/queryAttachments?token={}'.format(self.token)])

    # Url para la eliminacion de registros de ficha POG
    @property
    def delete_url_GPT_MS_POG(self):
        return ''.join([self.main_url, self.GPT_MS_POG, '/deleteFeatures?token={}'.format(self.token)])

    def __str__(self):
        return self.main_url

# import webbrowser
# url = "https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_867093e5f05e4186b76c27e8ac249bdb/FeatureServer/0?token=KKwULK0z9PHeLYMXV-EV9y5ACuui7rHGvhtnz2__6nlu1j3ZmOBkWjnGR2a4OKQ9HtG1DbAN7kgjurVBYzEoz3NcdZOoe9f7o1PCuaFvO6sKeEI4G2vnunqkXaCk7q5rNsFE_-Z6z_Zy5beFGq4EVYNtXFflY8hWyy7f2EDelJJFCwBtA7tlNL6C7WWeIaTWcBYMYWnSUBcJsWtLCzOLSA.."
# webbrowser.open_new(url)