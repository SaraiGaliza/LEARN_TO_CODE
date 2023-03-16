# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###
# Es una "plantilla" que sirve para definir las características y comportamientos de un objeto.
# Para definir las clases se usa CamelCase, en lugar de Snake_case como en las variables y las funciones

# Así se define una clase, utilizamos la palabra reservada "class":
class MyPerson:
    pass  # Con la palabra reservada "pass" poder dejar la clase vacía. Así "nos la saltamos". Es útil para saltarse un error en el cdfigo
print(MyPerson) # Podemos llamar a una clase de estas dos maneras
print(MyPerson())

# Ejemplo de clase con constructor de clase, funciones y popiedades privadas y públicas
class Person:
    # El siguiente trozo de código es el constructor de clase,la parte de "def_init_(Self" es obligatoria para poder construirla. 
    # Aunque contenga "def" en su inicio, no es una función, sino que es el trozo de código que sirve para que se definan las caracterísitcas de la clase person
    # La palabra "self" es obligatoria y hace referencia a la función que se haya definido, en este caso "person"
    def __init__(self, name, surname, alias="Sin alias"):
    # El siguiente trozo de código son las propiedades de la clase. Se definen con "self." Pueden ser públicas (de esta forma podemos accedera ellas fuera de la clase y también modificarlas) o pueden ser privada (de esta forma no podemos modficiarlas, y para accedera ellas necesitamos una función con return)
        self.__name = name  # Propiedad privada. Si escribimos una doble barra baja estamos haciendo que esa propiedad sea privada, entonces cuando queramos acceder a ella, no podresmo, Tenedmos que crear primero una funcion y luego hacer print de la funcion. Y solo podemos acceder, pero no podemos modificarlo 
        self.surname = surname  # Propiedad privada
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública (los paréntesis solo son para que se imprima el alias en el medio)
    # Para acceder a las propiedades a través de funciones tenemos que hacer referencia a la classe con la palabra "self"
    def get_name(self): # Si la propiedad es privada, para accedera a ella tenemos que definir una función que nos la devuelva. Y solo podemos acceder a esa propiedad fuera de la classe llamando a esta función. 
        return self.__name
    def walk(self): # Si la propiedad pública  se escribe así:
        return (f"{self.full_name} está caminando")
    def run(self):  # Función con print para una propiedad pública y otra privada:
        print(f"{self.full_name} está corriendo")
        print(self.__name + " " + self.surname)

# Una vez definida la clase, para poder accedera a ella tenemos crear una variable que la contenga y llamar a las propiedades o las funciones que hayamos definido. 
my_person = Person("Sarai", "Rodriguez") # Así creamos una varibale que contiene la clase definida anteriormente y nuevos valores.
print(my_person.full_name) # Así llamamos directamente a una propiedad pública que hemos definido anteiormente 
print(my_person.get_name()) # Así llamamos a una propiedad privada que hemos definido anteiormente.
print(my_person.walk()) # Así llamamos a la función pública que hemos definido anteiormente. 
my_person.run() # Así tamibén podemos llamar a una función, no hace falta un print, porque ya está definido dentro.

# Otras cosas de las funciones
my_other_person = Person("Sarai", "Rodriguez", "GalizaSarai") #Al escribir ahora un string en el alias, este se sobreescribe
print(my_other_person.full_name) # Esto devuelve todo el normbre con el neuvo alias
my_other_person.walk()
my_other_person.full_name = "Mi perrita Zoe (es la mejor perrita de todas)" # Aí estamos reescribiendo todo el full name
print(my_other_person.full_name) 
my_other_person.full_name = 666  # Aí estamos reescribiendo todo el full name
print(my_other_person.full_name)
