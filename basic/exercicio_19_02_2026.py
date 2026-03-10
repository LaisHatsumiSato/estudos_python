# print("Contadores de números pares e impares")
# numero=int(input("Digite um número: "))

# impar=0
# par=0
# for numeros in range(1,(numero+1)) :
#     if numeros % 2 != 0:
#         impar+=1
#     else:
#         par+=1
# print(f"PAR: {par}, IMPAR:{impar}")

# print("Número secreto")
# numero_secreto=7
# numero_digitado=int(input("Tente adivinhar o número secreto: "))

# while numero_digitado != numero_secreto:
#     numero_digitado=int(input("Tente adivinhar o número secreto: "))
#     if numero_digitado == numero_secreto: 
#         print("Parabéns! Você acertou!")

# todo acumulador em soma recebe 0 e se for multiplicação 1 porque não alteram o resultado
# print("Fatorial")
# numero=int(input("Digite um número: "))
# fatorial=1
# for i in range(1,numero):
#     fatorial= fatorial*i
# print(fatorial)

# print("Verificador de senha")
# senha_correta="python123"
# senha=input("Digite a senha: ")

# while senha != senha_correta:
#     print("Que pena! Tente novamente.")
#     senha=input("Digite a senha: ")
# print("Acesso liberado")

# print("Média até digitar 0")
# contador=0
# total=0
# while True:
#     numero=int(input("Digite um valor (0 para): "))
#     if numero!=0:
#         total+=numero
#         contador+=1
#     else:
#         break
# media=total/contador
# print(f"Média: {media} e a quantidade de números digitados: {contador}")

# print("Maior número digitado")
# maior=0
# for i in range(5):
#     numero=int(input("Digite um número: "))
#     if numero > maior:
#         maior=numero
# print(maior)

# print("Pirâmide")
# texto="*"
# texto_incremento="*"
# for i in range(5):
#     print(texto)
#     texto+=texto_incremento

print("Menu interativo")
