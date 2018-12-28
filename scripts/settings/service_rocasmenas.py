# -*- coding: utf-8 -*-

'''
Importacion de todas las librerias del 
proyect actual
'''
import os, requests, urllib, urllib2
import shutil, json, uuid
import arcpy
from bs4 import BeautifulSoup

# Url de servicios a utilizar
class Services(object):
    def __init__(self):
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

        self.token = "6ml7ukfH3QsE-VFUtGvmHy7WVQWXB2SwlsFcWe-Uqc2hDWFoG8_-Uu4-n5Gz8_EOV82xZ_0zB5mFQumrYWQMEpC52gFwjn48VDNzZpFc9Bv-myfMf8TJ6fRf-cmIGNiUGx0cvIoWgnniKUVIDPa7CrhJ4N5q9W7VRKACjRsfS72hoqaOPqU-RvXnVniJBJOXl0KVy3KunsdGUegOg7rujVY61zi9gqsnpeGL-d5JFfNkxjzaXijWtdZAiiMOquInYoIGs33WkO4LzouNWsj8lhulV9_M6fzhifyujEzJiRk."

    # Url para la eliminacion de registros
    @property
    def query_url_attach_Photos(self):
        return ''.join(
            [self.main_url, self.TB_RM_06_MULTIMEDIA, '/queryAttachments?token={}'.format(self.token)]
        )

    @property
    def delete_url_GPT_RM_ROCA_MENA(self):
        return ''.join([self.main_url, self.GPT_RM_ROCA_MENA, '/deleteFeatures/'])

    def __str__(self):
        return self.main_url


# import webbrowser
# poo = Services()
# url = poo.query_url_TB_RM_01_LITOLOGIA
# webbrowser.open_new(url)