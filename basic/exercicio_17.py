# print("Controle de fluxo")
# contador=0
# for i in range(5):
#     numero = float(input(f"Digite o {i+1}º número: "))

#     if numero>0:
#         contador+=1
# print(f"Quantidade de números positivos: {contador}")

# print("Média, 0 para a contagem")
# soma = 0
# quantidade=0

# numero=float(input("Digite um número(0 para parar): "))
# while numero !=0:
#     soma += numero
#     quantidade+=1

#     numero=float(input("Digite um número(0 para parar): "))

# if quantidade >0:
#     media = soma /quantidade
#     print(f"Média: {media}")
# else:
#     print("Nenhum número válido foi digitado.")

# print("Validador de número")
# validador_numero=int(input("Digite um número: "))
# while validador_numero <=0:
#     print("Número inválido")
#     validador_numero=int(input("Digite um número: "))
# print("Número válido")

# print("Login com tentativas limitadas 3x")
# senha=input("Digite a senha: ")
# senha_correta="123"
# tentativas= 3
# contador = 0
# while contador < 2:
    
#     if senha != senha_correta:
#         contador +=1
#         tentativas -=1
#         senha=input(((f"Usuário não autorizado. Restam {tentativas}"), { True: 'tentativa:', False: 'tentativas:'}[tentativas<2] ))
#     else:
#         print("usuário autorizado")
# print("Senha bloqueada")


