# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### TIPOS DE DATOS ###
# Phyton es un lenguaje de tipado dinámico (o tipado débil). Esto queire decir que podemos reescribir y modificar un tipo dato definicido previamente.

# Para consultar el tipo de dato usamos la funcion 'type'
print(type(10))                  # Int (entero)
print(type(3.14))                # Float (decimal)
print(type(1 + 3j))              # Complex (Complejo)
print(type('Dato str'))          # String (texto) = Son cadenas de texto. También acepta comillas dobles "dato str"
print(type(True))                # Bool (boleano) = Cuando es verdadero o falso
print(type([1, 2, 3]))           # List (lista) = Lista de elementos
print(type((10, 3.14, 6.345)))   # Tuple (tupla) = Lista de elementos
print(type({9.8, 3.14, 2.7}))    # Set (set) = Lista de elementos
print(type({'name':'Asabeneh'})) # Dictionary (diccionario) = Lista de elementos clave-valor

print(type(print('Mi cadena de texto')))  # 'NoneType'= Esto no se que es XD 

# Podemos reescribir un tipo de dato
dato_int = 10
dato_int = str(dato_int) # De esta forma cambiamos un tipo de dato 'int' a un 'str'
print(dato_int) # Imprime: 10 
print(type(dato_int)) # Imprime: Type 'str'


# También tenemos diferentes formas de dejar comentarios (anotaciones de código que no se ejecutan).
# Esto es un comentario
## Esto también es un comentario
"""
Esto es un
comentario
en varias líneas
"""
'''
Esto también es un
comentario
en varias líneas
'''
