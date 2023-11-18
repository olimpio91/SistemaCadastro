import sqlite3

class DataBase:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('Users.db')
            self.cur = self.conn.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS Registered(id INTEGER PRIMARY KEY AUTOINCREMENT,FirstName VARCHAR(50) NOT NULL , LastName VARCHAR(50) NOT NULL, User VARCHAR(50) NOT NULL, PassWord VARCHAR(100) NOT NULL)")
        except:
            print('Erro de conexão com banco de dados')



if __name__ == '__main__':

    responde = DataBase()