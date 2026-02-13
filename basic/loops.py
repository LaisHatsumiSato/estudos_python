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

# for i in range(2, 21, 2):
    # print(i)

print("Lista simples")
nomes= ["Ana", "Bruno", "Carlos", "Diana"]
for nome in nomes:
    print(f"Olá, {nome}")

print("Soma de Valores")
cont = 0
for i in range(0, 101):
     cont += i
     print(cont)

print("Contagem regressiva")
for j in range(6, 0, -1):
    print(j)

#Exercicios com while

print("Contador Simples while")
n=0
while n < 5:
    n +=1
    print(n)

print("Senha")
senha="123"
senhas = input("Digite sua senha: ")
while senha != senhas:
    senhas = input("Senha incorreta, por favor digite a sua senha:")
print("Senha correta!")

print("Menu")
print("1 - Ver saldo")
print("2 - Depositar")
print("3 - Sair")
escolha = int(input("Digite a sua escolha: "))
while  escolha != 3:
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sair")
    escolha = int(input("Digite a sua escolha: "))
    
print("Soma até parar(obs se quiser parar digite 0)")
a = float(input("Digite o primeiro valor: "))
soma=a
while a != 0:
    a = float(input("Digite valor para soma: "))
    soma += a 
print(soma)

print("Contagem regressiva controlada")
regre = int(input("Digite um número: "))
while regre > 0:
    regre-=1
    print(regre)