# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### VARIABLES ###
# Las variables son direcciones de memoria en las que se almacenan datos (cualqueir tipo de dato). Se recomienda usar variables memotécnicas (fáciles de recordar y ascoiar). Para nombrar una variable en python hay que seguir algunas reglas:
    # No se permiten números, caractéres especiales o guiones al inicio. siempre debe empezar por una letra o guión bajo
    # Solo están permitidos los caractéres alfanuméricos y los guiones bajos
    # No podemos usar palabras reservadas para declarar variables o funciones
    # Se recomienda usar nombres descriptivos (Edad, apellido, dirección) y evitar los cortos (a, x, sjnd)
    # Distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y FIRSTNAME) son variables diferentes

# Ejemplos de variables
string_variable_01 = "Cadena de texto"
print(string_variable_01) # Imprime: Candea de texto

int_variable_01 = 5
print(int_variable_01) # Imprime: 5

# Podemos cambiar/forzar un tipo de dato
variable_int_to_str = str(int_variable_01) # De esta forma creamos una nueva variable, cambiando un dato 'int' a un 'str'
print(variable_int_to_str) # Imprime: 5 
print(type(variable_int_to_str)) # Imprime: Type 'str'

bool_variable_01 = False
print(bool_variable_01) #Imprime: False

# Podemos concatenarvariables en un print
print(string_variable_01, variable_int_to_str, bool_variable_01)
print("Este es el valor de:", bool_variable_01)

# Algunas funciones del sistema
print(len(string_variable_01))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))
