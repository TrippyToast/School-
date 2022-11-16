#forgotPWD method was not impleemented as not too sure what the method is supposed to do
#ONLY WORKS with text databases, can add a selection statement within each method to change depending on database type



import csv
from datetime import datetime
from re import S
import hashlib
from random import choice

class dbAccess:#only currently works for text based databases

    def __init__(self, file): #only attrivute for the access class is the location of the database
      
        self.DB = file     #for just 1 database, put the name of the file when you initialise an objecy, has to be text file rn, if doesnt exist, empty text file will be created
        self.SECRET = "NoBugsAllowed"   #doesnt matter what this is
        self.ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


    def getDBConnection(self, mode):
        return(open("test.txt", mode, encoding = "utf-8"))


    def AddUser(self, userName, password):
        userExistscheck = self.userExists(userName)
        if userExistscheck == False:  #will only add if username is not already used, username acts as primary key
            salt = self.generateSalt() #create salt
            dbPwd = password + self.SECRET + salt  # intermediary step so next line is neater
            encPwd = hashlib.md5(dbPwd.encode()).hexdigest() #actual encoding
            userDate = str(datetime.now())
            rowtoInsert = userName + "," + str(encPwd) + "," + str(salt) + "," + userDate + "\n"    #creates a full line so all data for 1 user is in 1 line in the text file
            f = self.getDBConnection(mode = 'a') #appending
            f.write(rowtoInsert)
        else:
            print("Error adding user, username already in use") 

    def getUser(self, userName):  # returning all details about a user
        if userName == "" or userName == None: #not actually needed
            return None

        else:
            data = self.grabtbl() #getting the full database as a list(record) of lists(individual data values)
            for row in data: #iterating through each list(record)
                if row[0] == userName:#row[0] is the positiion of username as seen on line 27
                    return(row)

    def userExists(self, userName): #checks if a record has the username
        row = self.getUser(userName)
        if row == None:
            return(False)

        else:
            return(True)

    def validateUser(self, userName, plaintextPwd):
        salt = self.getSalt(userName) 
        intPwd = plaintextPwd + self.SECRET + salt
        encPwd = hashlib.md5(intPwd.encode()).hexdigest()
        hashedPwd = self.getHashPwd(userName)
        if encPwd == hashedPwd: #returns true if password is correct for given username
            return(True)

        else:
            return(False)

    def getSalt(self, userName):   #all these are just to make things easier if there were to be new methods created that would require the different data values
        data = self.getUser(userName)
        salt = data[2]
        return(salt)

    def getDate(self, userName):
        data = self.getUser(userName)
        date = data[3]
        return(date)

    def getHashPwd(self, userName):
        data = self.getUser(userName)
        encPwd = data[1]
        return(encPwd)


    def grabtbl(self):  #returns the whole database as a list of lists
        f = self.getDBConnection(mode = "r")
        data = csv.reader(f)
        tbl = []
        for row in data:
            tbl.append(row)

        return(tbl)

    def viewtbl(self): #prints entire database just for development testing
        tbl = self.grabtbl()
        for row in tbl:
            print(row)
            
    def wipetbl(self): #reset database just for development testing
        f = self.getDBConnection(mode = "w")
        f.truncate()
        f.close()

    def generateSalt(self):
        chars=[]
        for i in range(5):
            chars.append(choice(self.ALPHABET))
            
        return "".join(chars)
