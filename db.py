# 1° passo devo importar o banco de dado sqlite
import sqlite3 as lite

# 2° Passo criar a conexão
con = lite.connect('dados.db')

# 3° passo criar a tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, rg FLOAT, cpf FLOAT, veiculo TEXT, casa INT, hora_entrada DATE TIME, hora_saida DATE TIME)")