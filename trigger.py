from scripts.response_Geopedologia2 import *
from scripts.response_FuenteAgua import *
from scripts.response_RocasMenas import *

def process(module):
    poo = module
    poo.main()

def executeProcess(modulo, codes):
    response = None
    if modulo == "DRME_ROCASMENAS":
        response = Response_RocasMenas([codes])
    elif modulo == "DGR_GEOPEDOLOGIA":
        response = Response_Geopedologia([codes])
    elif modulo == "DGAR_FUENTEAGUA":
        response = Response_FuenteAgua([codes])

    # try:
    if codes == "CONTEO":
        listCDMTRA = response.sampleCounting()
        arcpy.AddMessage(listCDMTRA)
        arcpy.SetParameterAsText(2, listCDMTRA)
    else:
        process(response)
        arcpy.SetParameterAsText(2, "")
    # except Exception as e:
    #     arcpy.AddMessage("\n\t" + str(e))

# if __name__ == "__main__":
#     executeProcess()