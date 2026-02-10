contador = 10
while contador >= 0 :
    print(f"Contando: {contador}")
    contador-=1

#Loops
#é a repetição de uma mesma ação por x vezes, sem precisar ficar reescrevendo o código várias vezes.
#  "Enquanto isso for verdade, continue fazendo isso"
# Quando  usar, sempre que algo precisar acontecer mais de uma vez.
#   Você está copiando e colando a mesma linha várias vezes
#   Você não sabe quantas vezes algo vai se repetir
#   Existe uma condição pra parar
#   Você está lidando com listas, números, ou repetições
#  for quando vc sabe quantas vezes vai repetir
# while quando vc não sabe quntas vezes vai repetir
for i in range(11):
    print (i)

# #o for começa no número indicado que é 1 e termina no 9
for n in range(1,10):
    print(n)

print("Contagem personalizada só par")
for i in range(1, 21):
    if i % 2 == 0 :
        print(i) 

print("Lista simples")
nomes= ["Ana", "Bruno", "Carlos", "Diana"]
for nome in nomes:
    print(f"Olá, {nome}")

