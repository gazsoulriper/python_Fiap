equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print(f"\n Equipamento: {indice+1}")
    print(f"Nome: {equipamentos[indice]}")
    print(f"Valor: {valores[indice]}")
    print(f"Serial: {seriais[indice]}")
    print(f"Departamento: {departamentos[indice]}")
