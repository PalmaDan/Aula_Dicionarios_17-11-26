dicPessoa={"nome":"Joao", "idade":16 , "morada":"rua da atec"}

print("dicionario original: ", dicPessoa)

print("key nome original: ", dicPessoa ["nome"])

dicPessoa["nome"]="Pedro"

print("valor na key nome: modificado: ", dicPessoa["nome"])

print("valor na key idade: original: ", dicPessoa["idade"])

dicPessoa["idade"]=25

print("valor na key idade: modificado: ", dicPessoa["idade"])

print("mostra todas as keys no dicionario: ", dicPessoa.keys()) #Mostra todas as keys
print("mostra todos os valores no dicionario: ", dicPessoa.values()) #Mostra todos os valores em dicionario
print("mostra todo o dicionario: ", dicPessoa.items()) # mostra todo o dicionario
print("mostrar o valor da key escolhida: ", dicPessoa.get("idade")) # mostra valor na key idade
print("Remover valor e key idade: ", dicPessoa.pop("idade")) # remove key e value
print("tudo dicionario : ", dicPessoa)

dicPessoa.update({"idade":25}) # copia o valor e cria uma nova key "nif" com o valor da key "n"

print("todo dicionario : ", dicPessoa)

print(len(dicPessoa)) # tamanho do dicionario

for key, value in dicPessoa.items():
    print("key: ", key , "Value: ", value)