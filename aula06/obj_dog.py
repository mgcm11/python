from classe_dog import Dog

# Para criar o obj, utilizamos a variavel pastor e realizamos o processo de instanciaçao
# da classe dog.
# Foi passado o nome e a idade do 
pastor = Dog("Bob",2)
# acessamos o metodo data_dog que mostra 
# os dados do cachorro
pastor.data_dog()
pastor.sit()
pastor.roll_over()
print(pastor.__class__)
print(pastor.__dict__)