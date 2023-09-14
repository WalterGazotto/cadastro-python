import sqlite3 as lite

con = lite.connect('db.py')

dados = ['walter', '48.847.768-8', '420.789.748-89', 'civc', '01', '10/02/2023 07:00', '10/02/2023 07:05']

# inserir dados
with con:
    cur = con.cursor()
    query = "INSERT INTO cadastro(nome, rg, cpf, veiculo, casa, hora_entrada, hora_saida) VALUES(?,?,?,?,?,?,?)"
    cur.execute(query,dados)
    