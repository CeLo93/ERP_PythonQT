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
cliente = 'Maria Betânia'
cidade = 'Pedro Leopoldo'
idCliente = '10'


# UPDATE TABELA
print('UPDATE CLIENTE ')
sql = "UPDATE cliente SET Cidade = %s, Nome = %s WHERE idCliente = %s"
val = (cidade, cliente, idCliente)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record(s) updated')
