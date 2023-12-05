# Criaçao da classe Dog que dara origim
# a varios cachorros
class Dog:
    # Criaçao da funçao __init__ que 
    # È responsavel por inicializar o 
    # objeto que sera criado
    # esta sendo pedido o nome da e a idade do dog
    # no momento que ele é criado
    # Usamos o termo self para fazer uma 
    # referencia a propria classe 
    # Portanto, quando criar o dog e passar o nome e a idade , elas pertencerao a classe dog
    def __init__(self, name , age):
        self.name = name 
        self.age = age 
    
    def data_dog(self):
        print(self.name)
        print(self.age)

    def sit(self):
         print("sentou")

    def roll_over(self):
        print("Rolou")
