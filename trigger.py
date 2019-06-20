from response import *

def executeProcess(modulo, codes):
    if codes == "CONTEO":
        listCDMTRA = sampleCounting(modulo)
        arcpy.AddMessage(listCDMTRA)
        arcpy.SetParameterAsText(2, json.dumps(listCDMTRA))
    else:
        response(modulo, codes).main()
        arcpy.SetParameterAsText(2, "")

# if __name__ == "__main__":
#     executeProcess("DRME_ANAPS", "ROY")
