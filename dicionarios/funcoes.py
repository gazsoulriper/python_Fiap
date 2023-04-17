def perguntar():
    return input((("O que deseja realizar?\n"
                   "<I> - Para Inserir um usuário\n"
                   "<P> - Para Pesquisar os usuários\n"
                   "<E> - Para Excluir um usuário\n"
                   "<L> - Para Listar um usuário: "))).upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input(
                                                         "Digite a ultima data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)

def pesquisar(pesquisa):
    for i in pesquisa.keys():
        print(i)


def excluir(nome):
    nome.clear()
    print(nome)
    print("O dicionário foi esvaziado!")


def listar(user):
    id = input("Digite a chave a ser consultada: ")
    for i in user.get(id):
        print(i)


def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
