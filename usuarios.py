import database


class Users:
    def __init__(self):

        self.c = database.DataBase()


    def insert_into (self, FirstName, LastName, User, PassWorld):

        self.c.cur.execute(f"SELECT COUNT(User) FROM Registered WHERE User == '{User}' GROUP BY User")
        response = self.c.cur.fetchall()
        
        
        for tupla in response:
            
            for i in tupla:
                
                if i >= 1:
                    return False

            else:
        
                self.c.cur.execute("INSERT INTO Registered (FirstName, LastName, User, Password) VALUES(?,?,?,?)",(FirstName,LastName,User,PassWorld))
                self.c.conn.commit()
                
                return True

    def check(self, user, password):
        
        self.c.cur.execute("SELECT User,PassWord FROM Registered")
        response = self.c.cur.fetchall()

        for users in response:
            
            if (user,password) == users:
                return True
            
        return False
            

if __name__ == '__main__':
    responde = Users()
    responde.insert_into('kaua','trindade','olimpio','123')