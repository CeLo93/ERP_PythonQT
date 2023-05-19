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

# DELETE TABELA
print('DELETE CLIENTE ')
sql = "DELETE FROM cliente WHERE idCliente = '5'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'record(s) deleted')
