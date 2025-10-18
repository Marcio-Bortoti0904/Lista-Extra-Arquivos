# Exercício 1.
print("Exercício 1:")
with open('perfil.txt','w') as conteudo:
    conteudo.write("Márcio Bortoti do Espirito Santo Júnior.\n")
    conteudo.write("Idade: 16\n")
    conteudo.write("Comida Favorita: Frango\n")
print("Arquivo funcionando perfeitamente.")

#Exercício 2.
print("Exercício 2:")
with open('perfil.txt','r') as arquivo:
    conteudo = arquivo.read()
print("----Usando read() para fazer a leitura---------")
print(conteudo)

#Exercício 3.
print("Exercício 3:")
sent = input("Como está se sentindo hoje?\nR: ")
with open('diario.txt','a') as arquivo:
     arquivo.write(f"{sent}\n")
print("Arquivo funcionando")

#Exercício 4.
print("Exercício 4:")
tarefa = input("Digite uma nova tarefa = ")
with open('tarefas.txt','a') as arquivo:
     arquivo.write(f"{tarefa}\n")
with open('tarefas.txt',"r") as arquivo:
     conteudo_completo = arquivo.read()
     print(" --- Usando . read () ---")
     print( conteudo_completo )

#Exercício 5.
print("Exercício 5:")
with open('tarefas.txt','r') as arquivo:
     variavel = 0
     for linha in arquivo:
         variavel += 1
     print(f"{variavel} linhas")

#Exercício 6.
print("Exercício 6:")
with open("tarefas.txt","r") as arquivo:
     conteudo = arquivo.read()
with open('copia.txt','a') as arquivo:
     arquivo.write(conteudo)

#Exercício 7.
print("Exercício 7:")
num = int(input("= "))
i = 0
with open('tabuada.txt','w') as arquivo:
     for i in range(10):
         i += 1
         arquivo.write(f"{num} x {i} = {num*i}\n")

#Exercício 8.
print("Exercício 8:")
with open('notas.txt','w') as arquivo:
     arquivo.write("8.5\n")
     arquivo.write("9.0\n")
     arquivo.write("7.5\n")
     arquivo.write("10.0\n")
     arquivo.write("6.0\n")
with open('notas.txt', 'r') as arquivo:
    notas = 0
    total = 0
    div = 0
    for linha in arquivo:
        nota = float(linha.strip())
        total += nota
        div += 1
media = total / div
print(f"Média: {media}")

#Exercício 9.
print("Exercício 9:")
palavra = str(input(" = "))
nome_de_arq = str(input(" = "))
try:
    with open(nome_de_arq, 'r') as arquivo:
         conteudo = arquivo.read()
    num = conteudo.count(palavra)
    if palavra in conteudo:
       print(f"A palavra '{palavra}' foi encontrada {num} vezes")
    else:
       print("Error!!!!!!!!!!!!!!A palavra não foi encontrada.")
except:
      print("Arquivo não existe.")
#Exercício 10.
print("Exercício 10:")
print("------Agenda de contatos---------\n1.Adicionar um novo contato(nome e telefone)\n2.Listar todos os contatos salvos.\n3.Buscar um contato pelo nome.")
opcao = int(input("Escolha uma opção = "))
if opcao == 1:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    with open("agenda.csv", "a") as arquivo:
         arquivo.write(f"{nome}, {telefone}\n")
    print(f"Contato '{nome}' adicionado com sucesso!")
elif opcao == 2:
     try:
         with open("agenda.csv", "r") as arquivo:
              conteudo = arquivo.readlines()
              if len(conteudo) == 0:
                 print("A agenda está vazia.")
              else:
                 print("\n------ Contatos Salvos ------")
                 for linha in conteudo:
                     conteudo_completo = linha.strip()
                     print(conteudo_completo)
     except FileNotFoundError:
            print("Nenhum contato encontrado (arquivo não existe ainda).")
elif opcao == 3:
     nome_busca = input("Digite o nome para buscar: ")
     with open("agenda.csv","r") as arquivo:
          conteudo = arquivo.read()
          print(f"O contato {nome_busca} é: {nome_busca in conteudo}")
else: 
    print("Opção inválida!!!!")
