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
        self.main_url = r'https://services1.arcgis.com/'
        self.fichaPOG = "IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_bf568784c0c24107bdd494850b234f3c/FeatureServer/0"
        self.fichaECO = "IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_bf568784c0c24107bdd494850b234f3c/FeatureServer/1"
        self.fichaMORFO = "IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_bf568784c0c24107bdd494850b234f3c/FeatureServer/2"
        self.fichaFOTO = "IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_bf568784c0c24107bdd494850b234f3c/FeatureServer/3"
        self.token = "CyUFUngzKjudRnplrS2rd3PU4-rHAzwypA93yzxg6q2LWY2XxTXlThyGhZXZ4VDctEN--Kiil-gXM8qa1HRKRt-JRdu0u8V1KG2fNriJFsQclNKkaFMBU709dABRLafYl5gykl4gM371K0ud8rOyGDmY3033ugBk7gzkr4iqscxS7odAGAw-YYrF6LNCEIF0fDUPmyPjFRRl21pZTwZl2RJI8whGTRnl2UuD-esqGDondiMtRBA-FE_JM8oAZHBI5Zsxm7kigDAvYK7NC46KlxYS3e-ZZkpvf5jGCmZt9Yc."

    # Url para la consulta de imagenes (Photos)
    @property
    def query_url_attach_Photos(self):
        return ''.join(
            [self.main_url, self.fichaFOTO, '/queryAttachments']
        )
    @property
    def query_url_data_Photos(self):
        return ''.join(
            [self.main_url, self.fichaFOTO, '/query']
        )
    @property
    def delete_url_Photos(self):
        return ''.join(
            [self.main_url, self.fichaFOTO, '/deleteFeature']
        )
    # Url para la consulta de ficha POG
    @property
    def query_url_fPOG(self):
        return ''.join(
            [self.main_url, self.fichaPOG, '/query']
        )
    # Url para la eliminacion de registros de ficha POG
    @property
    def delete_url_fPOG(self):
        return ''.join(
            [self.main_url, self.fichaPOG, '/deleteFeatures/']
        )
    # Url para la consulta de ficha ECO
    @property
    def query_url_fECO(self):
        return ''.join(
            [self.main_url, self.fichaECO, '/query']
        )
    # Url para la eliminacion de registros de ficha ECO
    @property
    def delete_url_fECO(self):
        return ''.join(
            [self.main_url, self.fichaECO, '/deleteFeatures/']
        )
    # Url para la consulta de ficha MORFO
    @property
    def query_url_fMORFO(self):
        return ''.join(
            [self.main_url, self.fichaMORFO, '/query']
        )
    # Url para la eliminacion de registros de ficha ECO
    @property
    def delete_url_fMORFO(self):
        return ''.join(
            [self.main_url, self.fichaMORFO, '/deleteFeatures/']
        )
    def __str__(self):
        return self.main_url


# import webbrowser
# url = "https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_867093e5f05e4186b76c27e8ac249bdb/FeatureServer/0?token=KKwULK0z9PHeLYMXV-EV9y5ACuui7rHGvhtnz2__6nlu1j3ZmOBkWjnGR2a4OKQ9HtG1DbAN7kgjurVBYzEoz3NcdZOoe9f7o1PCuaFvO6sKeEI4G2vnunqkXaCk7q5rNsFE_-Z6z_Zy5beFGq4EVYNtXFflY8hWyy7f2EDelJJFCwBtA7tlNL6C7WWeIaTWcBYMYWnSUBcJsWtLCzOLSA.."
# webbrowser.open_new(url)
