import platform
import getpass
from datetime import datetime

print("Nome da maquina.............:", platform.node())
print("Arquitetura.................:", platform.architecture())
print("Sistema Operacional.........:", platform.system())
print("Versão do SO................:", platform.release())
print("Processador.................:", platform.processor())
print("Versão do Python............:", platform.python_version())
print("")
print(datetime.now())
print("")

usuario = getpass.getuser()
print(f"Login: {usuario}")
senha = getpass.getpass("Digite sua senha")
if usuario == "alxsv" and senha == "Hello":
    print("Seja bem vindo!")
else:
    print("Login ou senha não conferem. Acesso Negado!")