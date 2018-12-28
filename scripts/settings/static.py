# -*- coding: utf-8 -*-

'''
Importacion de todas las librerias
'''

import os, requests, urllib, urllib2
import shutil, json, uuid
import arcpy
from bs4 import BeautifulSoup

BASE_DIR = os.path.normpath(os.path.join(__file__, '../../..'))     # Directorio principal del proyecto
IMAGE_FORMAT = '.jpg'                                               # Formato de imagen

# Rutas de directorios que contiene archivos estaticos
class Statics(object):
    def __init__(self):
        self.path = os.path.join(BASE_DIR, 'statics')               # Directorio de archivos estaticos
        self.img = os.path.join(self.path, 'img')                   # Directorio de imagenes descargadas
        self.conn = os.path.join(self.path, 'BD_GEOCIENTIFICA.sde') # Geodatabase coorporativ
        self.scratch = arcpy.env.scratchGDB                         # Geodatabase temporal

        self.ds = 'DATA_EDIT'

    def __str__(self):
        return self.path