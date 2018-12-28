from scripts.response_Geopedologia import *


def process(codes):
    poo = Response(codes)
    poo.main()
    # poo.deleteAgol()

def executeProcess(codes=None):
    try:
        process(codes)
    except Exception as e:
        arcpy.AddMessage("\n\t" + str(e))

if __name__ == "__main__":
    executeProcess()
