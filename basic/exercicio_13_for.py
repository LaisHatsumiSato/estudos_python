# Exercicios 12/02/2026
print("Contar Vogais")
palavra=(input("Digite uma palavra: "))
vogais=["a","e","i","o","u"]
contador=0
for letra in palavra:
    if letra in vogais:
        contador+=1
print(f"Resultado: {contador} vogais")

print("Taduada com for")
tabuada=int(input("Digite um número para tabuada: "))
multiplicador=0
for i in range(multiplicador,10):
    multiplicador+=1
    resultado=tabuada*multiplicador
    print(f"{tabuada} * {multiplicador} = {resultado}")
