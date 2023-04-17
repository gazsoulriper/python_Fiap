from ftplib import *

ftp = FTP("ftp.ibiblio.org")
print(ftp.getwelcome())

user = input("Digite o login: ")
senha = input("Digite a senha: ")

ftp.login(user, senha)
print("Diretório atual de trabalho: ", ftp.pwd())
ftp.cwd("pub")
print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines("LIST"))
ftp.quit()