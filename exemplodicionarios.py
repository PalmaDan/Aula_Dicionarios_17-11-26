import os
import json as manipjson
idade=""
morada="" # {"idade":12, "morada":"Rua do desespero"}
dicpessoa={}
opc=""
sair=0
filename=R"C:\DEV\Python\UFCD - 10793\dicionario.json"

if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as manipfiler:
        dicpessoa=manipjson.local(manipfiler) # ler do file para a variável dicpessoa


while sair==0:
    print("prima 1 para inserir nome ")
    print("prima 2 para Listar nome ")
    print("prima 3 para Apagar nome ")
    print("prima 4 para sair e Gravar no file ")
    print("prima 5 para Sair ")
    opc=input("intrud opção ")
    match opc:
        case "1":
            nome=input("insere nome") # permitir a introdução de várias pessoas
        case "2":
            print(nome) # mostrar com um for each os valores(pessoas, outras coisas etc...) do dicionario
        case "3":
            nome=""
        case "4":
            with open(filename, 'w+', encoding='utf-8') as manipfilew:
                # json.dump salva o dicionario no arquivo como texto JSON
                # indent=4 deixe o JSON formatado
                # f: e o file handler, o arquivo aberto em modo escrita "w"
                # ensure_ascii=false permite acentos e caracteres especiais
                manipjson.dump(dicpessoa,manipfiler,indent=4,ensure_ascii=False)
                sair=1
        case "5":
            print("Fechando programa")
            sair=1
        case _:
            print("opção errada")