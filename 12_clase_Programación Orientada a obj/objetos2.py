class Persona:
    pass

class Dog:
    tipo = "mamifero"
    cantidad_ojos = 2

#Métodos especiales:
    def __str__(self):
        return f"Yo soy un perro de raza {self.raza} y de color {self.color}"
    def __iter__(self):
        for ra in self.raza:
            yield ra

    def __len__(self):
        return len(self.raza)

#Atributos
    def __init__(self, raza: str, color: str, duenio: Persona) -> None:
        self.raza = raza
        self.color = color
        self.cantidad_patas = 4
        self.duenio = duenio
        

#funiconalidades
    def ladrar(self) -> str:
        if self.raza == "doberman":
            return "gggggggg"
        return "wofff"

                                #@staticmethod
    def caminar(self, cantida_pasos): #o def caminar(cantida_pasos):
        if cantida_pasos > 100 and self.raza == "doberman" :   #Tengo que definirla si no lo esta en los atributos
            return "ha caminado mucho"
        return "ha caminado poco"

print(Dog.tipo)

print("--------------")

dog_1 = Dog(raza="doberman", color="Negro")
print(f"1. {dog_1}")
print(dog_1.raza)
print(dog_1.color)
print(dog_1.ladrar())
print(dog_1.caminar(500))
print(len(dog_1))

print("--------------")

dog_2 = Dog(raza="Pastor aleman", color="Blanco")
print(dog_2.raza)
print(dog_2.color)
print(dog_2.ladrar())


