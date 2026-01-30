def soma (n1,n2):
    adicao=n1+n2
    print(f'A soma dos números: {n1} e {n2} é {adicao}')
    return adicao
print(soma(1,2))

valor=2
valor2=2
def somar(valor,valor2):
    mais=valor+valor2
    return mais
print(somar(valor,valor2))

nome="Lais"
def saudar(nome):
    print(f"Olá! {nome}, Seja bem vinda!")
saudar(nome)

numero=int(input("Digite um numero para calculo de subtração: "))
numero2=int(input("Digite o segundo número: "))
def subtracao(numero,numero2):
    resultado = numero - numero2
    print(f"O primeiro número digitado foi {numero}, o segundo {numero2} o resultado da subtração é: {resultado}")
    return resultado
subtracao(numero,numero2)

num1 = int(input("Digite um número para cálculo de multiplicação: "))
num2 = int(input("Digite o segundo número: "))
def multiplica(num1,num2):
    resultado_multi=num1*num2
    print(f"O primeiro número digitado foi {num1}, o segundo foi {num2} o resultado da multiplicação é {resultado_multi}")
    return resultado_multi
multiplica(num1,num2)

numero01=5
numero02=5
def numfixo(numero01,numero02):
    resultado_numfixo= numero01 + numero02
    print(f"Numero fixo: {numero01}, o segundo: {numero02} o resultado da soma é: {resultado_numfixo}")
numfixo(numero01,numero02)

name=input("Como se chama? ")
def mensagem(name):
    print(f"Olá, {name}. Seja bem vinda!")
mensagem(name)

a=int(input("Digite um número para ver o dobro dele: "))
def dobro(a):
    result_dobro= a*2
    print(f"O número digitado foi {a} o dobro é: {result_dobro}")
    return result_dobro
dobro(a)

c=5
d=5
def valor_externo(c,d):
    soma_vlr_extrno=c+d
    return soma_vlr_extrno
print(valor_externo(c,d))

def msg_fixa():
    print("Estudando python, funções")
msg_fixa()

a=3
b=3
def so_return(a,b):
    result_so_return=a+b
    return result_so_return
print(so_return(a,b))

x=4
def triplo(x):
    result_triplo=x*3
    print(f'O triplo de {x} é {result_triplo}')
    return result_triplo
print(triplo(x))