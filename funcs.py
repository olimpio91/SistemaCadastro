import psycopg2

def conexao_db():
    
    parametros = {
        'host' : 'localhost',
        'database' : 'Users',
        'user' : 'postgres',
        'password' : '992882381Km.'}

    try:
        con = psycopg2.connect(**parametros)

        print('Conexao feita com sucesso!')
    
    except:
        print('Erro na conexao')

if __name__ == '__main__':
    
    conexao_db()