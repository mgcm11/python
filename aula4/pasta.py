import os
os.system("clear")
os.system("rm -r dados_info")

os.mkdir("dados_info")

os.chdir("dados_info")

ar = open("texto.txt","x")

ar.write("hoje é sexta-feira")

ar.close()
os.getcwd()
print(os.getcwd())
print("dieretorio criado")