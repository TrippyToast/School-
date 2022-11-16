from dbClassV2 import dbAccess

def main():

    dbConn = dbAccess("%%%%%%.csv")     #replace %%%%%%% with the name of the database you want to create, or the name of the csv database you already have BUT next line below will wipe your database
    #dbConn.wipetbl()    

   
    
    names = ["apple", "bob", "carl", "derek", "eagle", "fly", "giraffe", "hippo"] 
    passwords = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for i in range(8):
        dbConn.AddUser(names[i], passwords[i])  #filling wiped database with logins

    
        
    #dbConn.viewtbl()
    print(dbConn.getUser("apple"))
    dbConn.AddUser("apple", "3")

    print(dbConn.validateUser("bob", "wrongpasswrod"))
    dbConn.viewtbl()
    dbConn.AddUser("hello", "12345")
    print(dbConn.getUser("hello"))
    

    
# driver code
if __name__ == "__main__":
    main()

