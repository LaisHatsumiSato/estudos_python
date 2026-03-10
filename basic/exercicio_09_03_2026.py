# Escrevendo em um arquivo
# with open ("exemplo.txt", "w") as arquivo:
#     arquivo.write("Primeira Linha do arquivo.\n")
#     arquivo.write("Segunda linha do arquivo.\n")

# Ler o conteúdo de um arquivo
# with open ("exemplo.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print("Conteúdo do arquivo: \n")
#     print(conteudo)

# ler linha por linha
# with open("exemplo.txt", "r") as arquivo:
#     print("Lendo linha por linha")
#     for linha in arquivo:
#         print(linha.strip())

# Acrescentando conteúdo ao arquivo
# with open("exemplo.txt", "a") as arquivo:
#     arquivo.write("Sexta linha adicionada.\n")

#Confirmando  leirua após append
with open ("exemplo.txt","r") as arquivo:
    print(arquivo.read())