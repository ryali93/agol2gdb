import sys
sys.path.insert(0, r'D:\APPS\WEBGIS_PIM\AGOL2GDB')

import trigger

codes = arcpy.GetParameterAsText(0)
trigger.executeProcess(codes)