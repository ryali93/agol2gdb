# Servicio de geoproceso que llamara al geoproceso alojado en el servidor
import sys
# Agregando archivos y scripts necesarios
sys.path.insert(0, r'D:\aplicaciones\geoproceso\BDGeocientifica')

# Funcionalidad para ser llamada como trigger de ser necesario
import trigger

if __name__ == "__main__":
    modulo    =  arcpy.GetParameterAsText(0) # Parametro que indica el modulo de la BDGeocientifica
    codes     =  arcpy.GetParameterAsText(1) # Codigos de cada modulo que se envian desde el agol a la BDGeocientifica

    trigger.executeProcess(modulo, codes)