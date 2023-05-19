import mysql.connector

# SCRIPT DE CONSULTA PADRAO AO BANCO DE DADOS---v

mydb = mysql.connector.connect(
    host="localhost",
    user="marcelo",
    password="1234",
    database="python"
)
# define o cursor do usuario, no caso define a entrega para a minha maquina e não outra que esteja utilizando o banco de dados
mycursor = mydb.cursor()
# ATÉ AQUI É PADRÃ0 ----------------------------------------------------------------^

# variaveis:
cliente = 'Kauã'
telefone = '33 9872522'
cidade = 'Rubelita'

# INSERT TABELA
print('INSERT CLIENTE ')
sql = "INSERT INTO cliente (Nome, Telefone, Cidade) values (%s, %s, %s)"
val = (cliente, telefone, cidade)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record(s) inserted')
