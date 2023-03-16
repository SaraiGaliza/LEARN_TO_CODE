# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### LOOPS ###
# Nos sirven para pasar por el mismo código varias veces. Tenemos de diferente s tipos: While, for, ¿do while? (creo que en python no lo tenemos)

# LOOP WHILE:
# ¿Cómo funciona? Mientras se cumpla la condicione definida haz esto. En el momento que la condicion dada sea falsa, las líneas de código debajo del while se coninuarán ejecutandose.

variable_01 = 0

while variable_01 < 10: # ¿Variable_01 es menor que diez? Si
    print(variable_01) # Pues lo imprimimos
    variable_01 += 2 # Sumamos 2 a la variable y el loop vuelve a empezar con un nuevo valor en variable_01. Si no hacemos esta parte el ciclo tendería a infinito (porque la variable siempre sería 0, y 0 es memor que 10) y petaría el ordenador.
else:  # Es opcional. Esto no lo tienen todos los lenguajes. Es lo mismo que poner el print en otra línea fuera del bucle. El cliclo while acepta el "else" pero no acpeta el "if" o el "elsif"
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while variable_01 < 20:
    variable_01 += 1
    if variable_01 == 15:
        print("Se detiene la ejecución") # Si la ejecución llega a 15, no se imprime 15. Se imprime "se detiene la ejecución"
        break # Esta palabra reservada sirve para detener la ejecución 
    print(variable_01)

print("La ejecución continúa")

# LOOP FOR:
# ¿Cómo funciona? Se va a repetir tantas veces como elementos tengamos. Cada vez que el for de una vuelta está accediendo a uno de los elementos

list_01 = [35, 24, 62, 52, 30, 30, 17]

for element in list_01:
    print(element)

tuple_01 = (35, 1.77, "Brais", "Moure", "Brais")

for element in tuple_01:
    print(element)

set_01 = {"Brais", "Moure", 35}

for element in set_01:
    print(element)

dict_01 = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in dict_01:
    print(element)
    if element == "Edad":
        break
else: # En el momento que antes ponemos un break, este else no vale de nada y no se va a imprimir
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in dict_01:
    print(element)
    if element == "Edad":
        continue # Es contrario al break, lo que hace es que continue el for saltándose lo que hay debajo (en este caso el "se ejecuta"). No es muy recomendable en otros lenguajes
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")

### EJERCICIOS ###
