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
