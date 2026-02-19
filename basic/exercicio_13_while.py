tabuada=int(input("Digite um número para tabuada: "))
contador = 0
while contador <= 9:
        contador+=1
        resultado=tabuada*contador
        print(f"{tabuada} * {contador} = {resultado}")

print("Soma dos pares")
numero = 1
soma=0
while numero <= 50:
    if numero % 2 == 0:
       soma += numero
    numero += 1
print(soma)