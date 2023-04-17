nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input(
    "Suspeita de doença infectocontagiosa? ").upper()

if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print(
        f"O paciente {nome} tem prioridade no atendimento e deve aguardar na sala reservada.")
elif idade >= 65:
    print(f"O paciente {nome} possui atendimento prioritário.")
elif doenca_infectocontagiosa == "SIM":
    print(f"O paciente {nome} deve aguardar na sala reservada.")
else:
    print(f"O paciente {nome} pode aguardar na sala comum.")
