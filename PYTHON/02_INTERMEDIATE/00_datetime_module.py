# Clase MoureDev en vídeo: https://youtu.be/TbcEqkabAWU
# GitHub 30 Days of Phyton: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/16_Day_Python_date_time/16_python_datetime.md

### Datetime ###
# Este módulo proporciona clases para trabajar con fechas y horas. Contiene funciones para analizar y formatear fechas y horas, y para realizar operaciones aritméticas con fechas y horas.

import datetime # acedemos directamente al módulo
print(dir(datetime))# Estas son las funciones que podemos utiliar: #MAXYEAR #MINYEAR #__builtins__ #__cached__ #__doc__ #__file__ #__loader__ #__name__ #__package__ #__spec__ #date #datetime #datetime_CAPI #sys #time #timedelta #timezone #tzinfo

# Así accedemos directamente a las funciones del módulo. Estas son algunas de las más usadas
from datetime import datetime #
from datetime import timedelta #
from datetime import date #
from datetime import time #

# Así trabajamos con la fecha actual. 
from datetime import datetime # Improtamos la función que queremos 
now = datetime.now()
print(now)
day = now.day
month = now.month               
year = now.year
now.hour
now.minute
now.second
timestamp = now.timestamp() # Is the number of seconds elapsed from 1st of January 1970 UTC.
print(day, month, year)
print(now.hour, now.minute, now.second)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}')

def print_date(date): # Así definimos una funcion con datos actuales de este momento, introduciendo el valor "now"
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
print_date(now)

# Así trabajamos con otra fecha
year_2023 = datetime(2023, 1, 1) # Necesitamos año, mes y día
print_date(year_2023)

# Time
current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

# Operaciones con fechas
diff = year_2023 - now
print(diff)
diff = year_2023.date() - current_date
print(diff)

# Timedelta
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

from datetime import timedelta # Diferencia entre dos fechas usando la funcion "timedelta"
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
   