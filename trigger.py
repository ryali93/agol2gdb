# importacion de clases, funciones y variables del archivo response
from response import *

# proceso de consulta o subida a la BDGeocientifica
def executeProcess(modulo, codes):
    if codes == "CONTEO":
        listCDMTRA = sampleCounting(modulo)
        arcpy.AddMessage(listCDMTRA)
        arcpy.SetParameterAsText(2, json.dumps(listCDMTRA)) # Devuelve un json del feature principal del modulo
    else:
        response(modulo, codes).main()
        arcpy.SetParameterAsText(2, "")

# if __name__ == "__main__":
#     executeProcess("DRME_ANAPS", "CONTEO")
