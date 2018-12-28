class Messages:
    def __init__(self):
        self.initFicha       = "\n\tStarting reading of service"
        self.waitresponse    = "\n\tWaiting for response from the service"
        self.updateRows      = "\n\tUpdating coordinates of records"
        self.insertdata      = "\n\tInsert rows into geodatabase"
        self.deleterows      = "\n\tDelete rows from service"
        self.finished        = "\n\tFinished..!"
        self.succesdelete    = '\n\tRows successfully removed: {}'
        self.faileddelete    = '\n\tThe record was not deleted: {}'
        self.successquery    = '\n\tSatisfactory query'
        self.failedquery     = '\n\tThe queried row is not found'
        self.response400     = '\n\tService page not found: 400'
        self.runtimeerror    = "\n\tProcess Error"
        self.loadimageaction = "\n\tGenerating load of images and actions"