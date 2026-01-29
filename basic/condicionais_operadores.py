# maior que ( > )
# maior ou igual >=
# igual ==
# menor que <
# menor ou igual <=
# diferente de !=

# condicionais compostas 
# AND - verifica se as duas expressoes passadas são verdadeiras
# OR - somente uma precisa ser verdadeira
# NOT - inverte afirmação ou negativa

# Idade
idade = int(input("Digite a sua idade: "))

def documento ():
    identidade = int(input("Está com documento? digite 1=sim e 2=não: "))
    if identidade == 1:
        print("(X) Sim")
        print("( ) Não")
    elif identidade == 2:
        print("( ) Sim")
        print("(X) Não")
    else:
        print("Opção inválida!")

    return identidade

identidade = documento()

if idade >= 18 and identidade == 1:
    print("Entrada permitida!")
elif idade >= 18 and identidade ==2:
    print("Por favor, apresentar o documento")
    identidade = documento()
    if identidade == 1:
        print("Entrada permitida!")
    else:
        print("Entrada não permitida")
else:
    print("Entrada não permitida")