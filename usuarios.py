import database

class Users:
    def __init__(self):

        self.c = database.DataBase()

    def insert_into (self, FirstName, LastName, User, PassWorld):
        
        self.c.cur.execute("INSERT INTO Registered (FirstName, LastName, User, Password) VALUES(?,?,?,?)",(FirstName,LastName,User,PassWorld))
        self.c.conn.commit()

    def check(self, user_entry, password_entry):
        
        user = user_entry
        password = password_entry

        response = self.c.cur.execute(f"SELECT User,PassWord FROM Registered where User == {user} AND PassWord == {password}")
        response.fetchall()
        print(response)


if __name__ == '__main__':
    responde = Users()
    responde.check('Paola','123')