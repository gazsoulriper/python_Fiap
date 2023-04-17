equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()
print("---------------------------------------")

busca = input("Digite o nome do equipamento: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print(f"Valor: {valores[indice]}")
        print(f"Serial: {seriais[indice]}")
        print(f"Departamento: {departamentos[indice]}")
    else:
        print("Equipamento não cadastrado.")
