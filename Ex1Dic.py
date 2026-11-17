# Ex1. Criar um dicionário simples

alunos = {}

while True:
    print("1- Inserir")
    print("2- Listar")
    print("0- Sair")
    opcao = input("Escolhe: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        alunos[nome] = {"idade": idade, "curso": curso}

    elif opcao == "2":
        for nome, dados in alunos.items():
            print("nome: ", nome)
            print("idade: ", dados["idade"])
            print("curso: ", dados["curso"])
            print()

    elif opcao == "0":
        break