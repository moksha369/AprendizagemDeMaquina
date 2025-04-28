#Criando o arquivo dados.csv
with open('dados.csv', 'w') as arquivo:
    arquivo.write('Nome,Idade\nAna,25\nBruno,30\nCarla,22\nDaniel,28\nEduardo,35')

#Ler o arquivo dados.csv e armazenar os dados em uma lista
dados = []
with open('dados.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]:  # Pulamos a primeira linha (cabeçalho)
        nome, idade = linha.strip().split(',')
        dados.append((nome, int(idade)))

#Solicitar o nome ao usuário via input
nome_digitado = input('Digite um nome: ')

#Verificar se o nome está na lista
encontrado = False
for nome, idade in dados:
    if nome == nome_digitado:
        encontrado = True
        idade_mais_velho = max(dados, key=lambda x: x[1])[1]
        if idade == idade_mais_velho:
            print(f'{nome} tem {idade} anos, é a pessoa mais velha da lista.')
        else:
            print(f'{nome} tem {idade} anos, não é a pessoa mais velha da lista.')
        break

#Mensagem se o nome não for encontrado
if not encontrado:
    print('Nome não encontrado na lista.')