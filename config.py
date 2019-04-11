from __future__ import print_function
import os

__author__ = 'Roy Marco Yali Samaniego'
__copyright__ = 'INGEMMET 2018'
__credits__ = ['Roy Yali S.']
__version__ = '1.0.1'
__maintainer__ = 'Roy Yali S.'
__mail__ = 'autonomoosi02@ingemmet.gob.pe'
__status__ = 'Product'

BASE_DIR = os.path.normpath(os.path.join(__file__, '..'))# Directorio principal del proyecto
STATIC_DIR = os.path.join(BASE_DIR, 'static')                  # Formato de imagen
IMAGE_FORMAT = '.jpg'                                          # Formato de imagen

conn = os.path.join(STATIC_DIR, 'conn/BD_GEOCIENTIFICA.sde') # Geodatabase coorporativa
