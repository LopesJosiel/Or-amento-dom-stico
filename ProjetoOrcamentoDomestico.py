# iniciando o projeto
print ('Bem-vindo ao mundo das finanças organizadas! Lembre-se de que os números não mentem')
#criando um input para receber as receitas
while True:
    receita_entrada = input('Digite valor e data da receita')
    receitas = float (receita_entrada)
    lista1 = []
    #criar um loop para armazenar cada entrada de receita
    for receita in receitas:
        lista1.append (receitas)
    print (lista1) #erro pois float não é iterável
    

#para criar conexão com o banco de dados

import mysql.connector
#criando o tratamento com o banco de dados

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
mycursor = mydb.cursor()

#inserir receitas
var_data = input('Escolha a data')
var_valor1 = input('qual o valor da receita')
var_valor = float (var_valor1)
var_descricao = input ('Qual a descrição da receita?')

com_insert_rec = f'INSERT INTO receitas (data, valor, descrição) VALUES ({var_data}, {var_valor}, "{var_descricao}")'
cursor.execute (com_insert_rec)
conexao.commit ()
#inserir despesas


comando = 'comando  sql'
cursor.execute (comando)
conexao.commit () #quando edito o banco de dados, não preciso quando leio
resultado = cursor.fetchall () #ler o banco de dados

cursor.close () # fechando cursor quanto for executado
conexao.close() #fechando conexão futura ao banco de dados