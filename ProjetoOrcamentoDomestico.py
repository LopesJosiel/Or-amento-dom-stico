# iniciando o projeto
print ('Bem-vindo ao mundo das finanças organizadas! Lembre-se de que os números não mentem')
#criando um input para receber as receitas
import mysql.connector
orcamentodemestico = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1035308",
  database="orcamentodomestico"
)
mycursor = orcamentodemestico.cursor()
entrada = input ('receita[r], despesa [d], saldo[s], fechar [f]') #entrada que definirá o caminho a ser seguido pelo programa
#criando o tratamento com o banco de dados
while entrada == 'r': #input da receita realizado com sucesso
    var_data = input('Escolha a data')
    var_valor1 = input('qual o valor da receita')
    var_valor = float (var_valor1)
    var_descricao = input ('Qual a descrição da receita?')
    com_insert_rec = f'INSERT INTO receita (data, valor, descricao) VALUES ({var_data}, {var_valor}, "{var_descricao}")'
    mycursor.execute (com_insert_rec)
    orcamentodemestico.commit ()
    mycursor.close () # fechando cursor quanto for executado
    orcamentodemestico.close() #fechando conexão futura ao banco de dados 


mycursor = orcamentodemestico.cursor()
#criando o tratamento com o banco de dados
while entrada == 'd': #input da receita realizado com sucesso
    var_data = input('Escolha a data')
    var_valor1 = input('qual o valor da despesa')
    var_valor = float (var_valor1)
    var_descricao = input ('Qual a descrição da despesa?')
    com_insert_rec = f'INSERT INTO despesa (data, valor, descricao) VALUES ({var_data}, {var_valor}, "{var_descricao}")'
    mycursor.execute (com_insert_rec)
    orcamentodemestico.commit ()
    mycursor.close () # fechando cursor quanto for executado
    orcamentodemestico.close() #fechando conexão futura ao banco de dados 


#mycursor = mydb.cursor()

#inserir receitas
#var_data = input('Escolha a data')
#var_valor1 = input('qual o valor da receita')
#var_valor = float (var_valor1)
#var_descricao = input ('Qual a descrição da receita?')

#com_insert_rec = f'INSERT INTO receitas (data, valor, descrição) VALUES ({var_data}, {var_valor}, "{var_descricao}")'
#cursor.execute (com_insert_rec)
#conexao.commit ()
#inserir despesas


#comando = 'comando  sql'
#cursor.execute (comando)
#conexao.commit () #quando edito o banco de dados, não preciso quando leio
#resultado = cursor.fetchall () #ler o banco de dados
#
#cursor.close () # fechando cursor quanto for executado
#conexao.close() #fechando conexão futura ao banco de dados