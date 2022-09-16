print("Clase 15-09-2022 = Calculadora de Raiz Cuadrada = Trabajo de Ruddy Contreras 21-1826")

import math
#Procedimiento en codigo para hacer poder elegir el numero
num1= int(input("Ingrese un primer numero: "))
num2= int(input("Ingrese el segundo numero: "))

#Procedimiento de potencia
num3= num1**2
num4= num2**2
raiz= math.sqrt(num3 + num4)


#Procedimiento de representacion del calculo
print("Nuestro primer numero es", num1)
print("Nuestro segundo numero es", num2)
print("La potencia de", num1, "es", num3 )
print("La potencia de", num2, "es", num4 )
print("La suma de estos resultado es", num3 + num4 )

#Nuestro resultado se mostrara por esta ultima linea
print("El resultado de √(a²+b²) es igual a", raiz)

input()
