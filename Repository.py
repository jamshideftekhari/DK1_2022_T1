import mysql.connector

class Repository(object):
    Dk1DB = object
    mycursor = object
    RowsList = []
    # to set connection up as student user on dk1studentuser  
    def SetConnection(self):
        self.Dk1DB = mysql.connector.connect(
                  host = "dk1sqlserver.mysql.database.azure.com",
                  user = "studentuser",
                  password = "Student123",
                  database = "dk1a2021"
                  )
        self.mycursor = self.Dk1DB.cursor()
    # to print all table elements  
    def GetAll(self):
        print(self.Dk1DB)
        # mycursor = self.Dk1DB.cursor()
        self.mycursor.execute("select * from student")
        personResult = self.mycursor.fetchall()
        for x in personResult:
            print(x)

    # to get all table elements as a list
    def GetAllTolist(self):   
        self.mycursor.execute("select * from student")
        RowsList = self.mycursor.fetchall()
        return RowsList     

    # add a row to the table.
    def AddRow(self):
        self.mycursor.execute(" insert into student (LastName, FirstName, Age, FavoritChips) values ('LName', 'FName', 00, 'Chips Name') ")
        self.Dk1DB.commit()
        print(self.mycursor.rowcount, " record inserted")
