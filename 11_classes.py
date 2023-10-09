## Classes ##

class MyEmptyPerson:
    pass   # <- se utiliza pass para definir una clase vacía

class Person:
    def __init__(self, name, surname, alias = "sin alias") -> None:
        
        self.__name = name    # con el doble guíón bajo __  haces privada la propiedad, de tal manera que no la puedes modificar de manera directa
        self.__surname = surname # con el doble guíón bajo __  haces privada la propiedad, de tal manera que no la puedes modificar de manera directa
        self.full_name = f"{name} {surname} ({alias})" # Propiedad Pública
    
    def walk (self):  # < - el parámetro self SIEMPRE es Requerido
        print(f"{self.full_name} está caminando")

    def get_name(self):         # GET < - esta es la forma de hacer un GET de las propiedades privadas __
        return self.__name
    
    def set_name(self, name):   # SET < - esta es la forma de hacer un SET  de las propiedades privadas __
        self.__name = name

my_person = Person("Juan", "Flores")   # Aquí se instancía la clase

#print(f"{my_person.name} {my_person.surname}")
print(my_person.get_name())
my_person.set_name("Fito")
print(my_person.get_name()) 
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Juan", "Flores","Devcodebrain")   # Aquí se instancía la clase

#print(f"{my_other_person.name} {my_other_person.surname}")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Malú Garza (Bombonete)"
print(my_other_person.full_name)
