#imprime o datatype do dado
print(type("Olá, Mundo!"))

#Todo input armazena string, para salvar com outro tipo de dado
# declarar o tipo de dado antes do input ex:
idade=int(input("Qual a sua idade? "))
print(idade)

#Tipos de dados
#string :  str = texto
#int : inteiro = valor numerico
#float : flutuante = valor decimal

# Variáveis
# são pequenos espaços de memórias usados para armazenar os dados. Ex:

frutas="Morango"
print(frutas)

#não podem ser iniciados com números, nem com caracteres especiais.
#é case sensitive

#Uso de f string 
#Para formatar o texto, ou seja, posso chamar uma variável dentro do print

nome="Lais"
print(f"Olá, {nome}. Seja bem vinda!")