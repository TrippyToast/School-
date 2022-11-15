class dbAccess:

    def __init__(self, file):
      
        self.DB = file
        self.SECRET = "NoBugsAllowed"
        self.ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


    def getDBConnection(self):
        

        return(open("test.txt", mode, encoding = "utf-8"))




