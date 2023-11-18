import database

class Users:
    def __init__(self):

        self.c = database.DataBase()

    def insert_into (self, FirstName, LastName, User, PassWorld):
        
        self.c.cur.execute("INSERT INTO Registered (FirstName, LastName, User, Password) VALUES(?,?,?,?)",(FirstName,LastName,User,PassWorld))
        self.c.conn.commit()
        self.c.conn.close()
    