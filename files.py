#ler do file

# Continuamos a utilizar o programa com antigamente
nome=""
filenome=R"C:\DEV\Python\UFCD - 10793\nome.txt"

#Abrir em file
with open(filenome, 'r', encoding='utf-8') as manipfiler:
    nome=manipfiler.read()

#Continuamos a utilizar o programa como antigamente
print(nome)

#nome = input("intrud o nome: ")
print(nome)

#no fim ou quando solicitado gravamos o file
with open(filenome, 'w') as manipflwr:
    nome=manipflwr.write(nome)
print(nome)

##
#nome= input("intrud o nome: ") #errado

#print(nome)


#######################################################################

# Persistência de dados com ficheiros (txt, json, csv)

# Passo 1: Abrir o ficheiro para leitura
# - Utiliza-se a função open() com o modo 'r' (read/leitura)
# - Exemplo: open("ficheiro.txt", "r")

# Passo 2: Realizar ações no ficheiro
# - Modos de abertura:
#   'r' -> leitura (read)
#   'w' -> escrita (write) - sobrescreve o conteúdo existente
#   'a' -> acrescentar (append) - adiciona ao final do ficheiro
#   'b' -> modo binário (pode ser combinado com outros, ex: 'rb')
#   'x' -> criar novo ficheiro - erro se já existir

# Passo 3: Fechar o ficheiro
# - Sempre fechar o ficheiro após o uso com close()
# - Exemplo: ficheiro.close()

#####################################################################