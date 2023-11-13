class Animal(object):
    adn = True

    def __init__(self, cantidad_ojos: int, tipo_piel: str) -> None:
        self.cantidad_ojos = cantidad_ojos
        self.tipo_piel = tipo_piel

    def respirar(self) -> int:
        """
        Cantidad de veces qye respira por minuto
        :return: int
        """
        return 30

    def correr(self) -> str :
        """
        Me dice de que forma corre
        :return:  str
        """
        return "Corre normal"

class Mamifero:
    def respirar(self) -> str:
        return "estamos respirando por la nariz"

class Gato(Mamifero, Animal):
    def __init__(self, cantidad_ojos: int, tipo_piel: str, color: str, raza: str) ->None:
        Animal.__init__(self, cantidad_ojos = cantidad_ojos, tipo_piel = tipo_piel)
        # ° super(): Es como colocar Animal
        self.color = color
        self.raza = raza

    # def respirar(self) -> int:
    #     return Animal.respirar(self)
    # Se toma el valor de retorno de Animal.respirar
class Ballena(Animal):
    def  correr(self) -> str:
        return "este animal no corre"

    def nadar(self) -> str:
        return "este animal nada lento"


gato = Gato(cantidad_ojos=2, tipo_piel= "peludo" ,color = "rojo", raza = "Siames")
print("Para el gato:")
print(gato.cantidad_ojos)
print(gato.tipo_piel)
print(gato.respirar())
print("----------------")
ballena = Ballena(cantidad_ojos=2, tipo_piel="Escamosa")
print("Para la ballena:")
print(ballena.correr())
print(ballena.nadar())
print(ballena.cantidad_ojos)


print(Animal.__mro__)
print(Gato.__mro__)
print(gato.respirar())


