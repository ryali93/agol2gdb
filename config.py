from __future__ import print_function
import os

__author__ = 'Roy Marco Yali Samaniego'
__copyright__ = 'INGEMMET 2018'
__credits__ = ['Roy Yali S.']
__version__ = '1.0.2'
__maintainer__ = 'Roy Yali S.'
__mail__ = 'ryali93@gmail.com'
__status__ = 'Product'

BASE_DIR = os.path.dirname(__file__)
conn = os.path.join(os.path.dirname(BASE_DIR), "config\\bdgeocat_publ_gis.sde")

IMAGE_FORMAT = '.jpg'                                          # Formato de imagen

# conn = os.path.join(STATIC_DIR, 'conn/BD_GEOCIENTIFICA.sde') # Geodatabase coorporativa