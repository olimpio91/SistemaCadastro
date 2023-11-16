import database

class Users:
    def __init__(self):

        self.c = database.DataBase()

    def insert_into (self,usuario, senha):
        
        self.c.cur.execute(f"INSERT INTO Registered (User, Password) VALUES({usuario},{senha})")
        self.c.conn.commit()
        self.c.conn.close()