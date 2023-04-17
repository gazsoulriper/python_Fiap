usuarios = {}
print(usuarios)

usuarios = {
    "chaves" : ["Chaves do 8", "24/12/2022", "Barril"],
    "quico" : ["Quico Flores", "20/12/2022", "Vila"],
    "florinda" : ["Dona Florinda", "24/12/2022", "Restaurante"]
}

print(usuarios)
print("###---###")
# consultar somente um usuário da lista
for i in usuarios.get("chaves"):
    print(i)
