import database

class Users:
    def __init__(self):

        self.c = database.DataBase()

    def insert_into (self, FirstName, LastName, User, PassWorld):
        
        self.c.cur.execute("INSERT INTO Registered (FirstName, LastName, User, Password) VALUES(?,?,?,?)",(FirstName,LastName,User,PassWorld))
        self.c.conn.commit()

    def check(self, user, password):
        
        self.c.cur.execute("SELECT User,PassWord FROM Registered")
        response = self.c.cur.fetchall()

        for users in response:
            if (user,password) == users:
                return print('encontrado')
        return print('não encontrado')
            

if __name__ == '__main__':
    responde = Users()
    responde.check('olimpio','123')