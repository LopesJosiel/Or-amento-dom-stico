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
    

