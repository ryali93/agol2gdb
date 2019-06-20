import sys
sys.path.insert(0, r'D:\aplicaciones\geoproceso\BDGeocientifica')

import trigger

if __name__ == "__main__":
    modulo    =  arcpy.GetParameterAsText(0)
    codes     =  arcpy.GetParameterAsText(1)

    trigger.executeProcess(modulo, codes)