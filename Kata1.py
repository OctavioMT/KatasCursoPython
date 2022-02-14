sum = 1 + 2 # 3
product = sum * 2
print(product)

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
# Se convierte la fecha a cadena para poder concatenarlo con el mensaje Today's date is: 
print("Today's date is: " + str(date.today()))

#input () es una funcion para capturar la informacion ingresada por el usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

#se debe de hacer un cast a int para poder imprimir la suma, si no se hace este cast la salida seria la concatenacion de los numeros, 
#ya que el input toma lo ingrasado por el usuario como cadena
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))

