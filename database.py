import sqlite3

class DataBase:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('Users.db')
            self.cur = self.conn.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS Registed (id SERIAL PRIMARY KEY AUTOINCREMENT, User VARCHAR(100) NOT NULL , Password TEXT NOT NULL")
        except:
            print('Erro de conexão com banco de dados')



if __name__ == '__main__':

    responde = DataBase()