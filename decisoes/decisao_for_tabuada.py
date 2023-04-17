numero = int(input("Digite um numero: "))

print(f"===== Tabuada do {numero} =====")

for i in range(10):
    print(f"{numero} x {i+1} = {numero*(i+1)}")
