# Sarai Rodriguez \ Introducción a la programación \ Tema 3 \ 

### PRIMERA PARTE ###
# Crear una función con tres parámetros que sean números que se suman entre sí.
# Llamar a la función en el main y darle valores.

print("EXERCISE 1: START")
def function_with_3_strings(param_1, param_2, param_3): # Ejemplo con print dentro de la funcion y strings
    complete_name = param_1 + param_2 + param_3
    print(complete_name) # Devuelve: SaraiRodriguezLago
function_with_3_strings("Sarai", "Rodriguez", "Lago") 

def function_with_3_int(param_1: int, param_2: int, param_3: float): # Ejemplo con print fuera y tipado de dato con int/float
    return (param_1 + param_2 + param_3)
result = function_with_3_int(5, 10, 10.5)
print(result)  # Devuelve: 25.5

### SEGUNDA PARTE ###
# Crear una clase coche.
# Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
# Una función que incremente el número de puertas que tiene el coche.
# Crear un objeto miCoche en el main y añadirle una puerta.
# Mostrar el número de puertas que tiene el objeto.

print("EXERCISE 2: START")
class Car: # Definición de clase coche 
    def __init__(self, doors:int): # Constructor de clase 
        self.door_number = doors # Variable privada
    def add_door (self): # Función para incrementar el nº de puertas
        self.door_number = self.door_number + 1  # Cada vez que añadimos una puerta, se suma a la varaible donde teníamos el número de puertas guardado
        return self.door_number # Mostramos el total de puertas 
my_car = Car (4)
print(my_car.add_door())
print(my_car.add_door())
print(my_car.add_door())
