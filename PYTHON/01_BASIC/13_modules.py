# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583
# GitHub 30 Days of Phyton: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md
# Documentación: https://docs.python.org/es/3/tutorial/modules.html

### Modules ###
# Un modulo es un archivo que contiene un conjunto de códigos o un conjunto de funciones que pueden incluirse en una aplicación.
# Nos sirven para no estar duplicando código entre ficheros y poder acceder desde unos a otros (siempre que tengamos acceso)
# Cada fichero (tiples.py, strings.py, funtions.py...) funciona como un módulo. También pueden ser librerías externas de FGitHub, de Python...)

# Para importar un módulo en Python, utilizamos la instrucción "import"
import my_module # No podemos acceder a ficheros/módulos que empiezan por números (11_functions)
# Una vez que se ha importado un módulo, se pueden utilizar sus funciones y variables en el programa.
my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")

# Si solo queremos acceder a una parte concreta de este fichero, por ejemplo una funcio:
from my_module import sumValue, printValue # Así accedemos a dos funciones 
sumValue(5, 3, 1)
printValue("Hola python")

# Podemos acceder a los modulos del lenguaje Phtyon con la misma sintaxys
import math
from math import pi as PI_VALUE # Con "as" renombramos la variable "pi" 
print(PI_VALUE)
print(math.pow(2, 8))
print(math.sin(1))

# Con los comandos "dir" y "math" podemos acceder a información de las funcionalidades del modulo.
print(dir(math)) # Con "dir" podemos conocer la lista de funcionalidades disponibles de un determinado módulo.
print(help(math)) # Con "help" conocemos la lista y también para que sirve cada cada funcionalidad

# Estons son algúnos de los módulos mas usados en Python:
import os # Este módulo proporciona una interfaz para el sistema operativo. Contiene funciones para trabajar con archivos y directorios, así como para configurar el entorno del sistema.
import sys # Este módulo proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y a funciones que interactúan con el intérprete.
import math # Este módulo proporciona funciones matemáticas avanzadas. Contiene funciones para trabajar con números complejos, funciones trigonométricas, funciones exponenciales y logarítmicas, y constantes matemáticas como π.
import datetime # Este módulo proporciona clases para trabajar con fechas y horas. Contiene funciones para analizar y formatear fechas y horas, y para realizar operaciones aritméticas con fechas y horas.
import re # Este módulo proporciona soporte para expresiones regulares. Las expresiones regulares son patrones de búsqueda que se pueden utilizar para buscar y manipular cadenas.
import json # Este módulo proporciona funciones para trabajar con el formato de datos JSON. Contiene funciones para analizar cadenas JSON y para generar cadenas JSON a partir de objetos Python.
import csv # Este módulo proporciona funciones para trabajar con archivos CSV. Contiene funciones para leer y escribir archivos CSV y para trabajar con datos CSV en forma de listas y diccionarios.
import urllib # Este módulo proporciona funciones para trabajar con URLs. Contiene funciones para abrir URLs, leer datos de URLs y enviar datos a URLs.
import socket # Este módulo proporciona funciones para trabajar con sockets. Los sockets son un mecanismo de comunicación entre procesos que se pueden utilizar para enviar y recibir datos a través de una red.
import random # Este módulo proporciona funciones para generar números aleatorios y para mezclar secuencias.