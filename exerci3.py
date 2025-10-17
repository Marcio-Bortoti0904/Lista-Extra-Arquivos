#Exercício 3.
print("Exercício 3:")
sent = input("Como está se sentindo hoje?\nR: ")
with open('diario.txt','a') as arquivo:
     arquivo.write(f"{sent}\n")
print("Arquivo funcionando")
