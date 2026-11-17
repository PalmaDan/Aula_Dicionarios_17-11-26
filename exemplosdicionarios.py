import os
import json as manipjason
idade=""
morada="" # ( "idade": 12, "morada" : "Rua do Desespero " )
dicopessoa={}
opc=""
filename=R"d:\DEV-Iokany\pyhton\UFCD-10793\Aula7(pre)\dicionario.json"
sair=0
if os.path.exists(filename):
        with open(filename, 'r',encoding='utf-8') as manipfiler:
            dicopessoa=manipjason.load(manipfiler) # Ler do file para a variavel dicpessoa
 
while sair==0:
    print("prima 1 para inserir nome")
    print("prima 2 para listar nome")
    print("prima 3 para apagar nome")
    print("prima 4 para sair e Gravar o file")
    print("prima 5 para sair e sem Gravar")
    opc=input("Intrud opção ")
 
 
    match opc:
        case "1":
            nome=input("Interira o Nome: ") #Permitir a intrud de pessoas
        case "2":
            print(nome) # mostra com um for eache as pessoas do dicionario
        case "3":
            nome="" # apagar a pessoa escolhida do dicionario
        case "4":
          with open(filename, 'r',encoding='utf-8' ) as manipfilew:
               # json.dum salva o diconário no arquivo com o texto JSON
               # idente= 4 deixa o JSON  formatado
               # f: É O file handler, o arquivo aberto em modo escrita "W".
               # ensure_ascii=False permite acentos e caracteres especiais
               manipjason.dump(dicopessoa,manipjason,indent=4, ensure_ascii=False) # indent=4 so organiza o file  e o 4 é o nivel de iidentação que precisas
               sair=1
        case "5":
            sair=1
        case _:
            print("Opeção invalida")
 