#Ruddy Contreras 21-1826
#Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. 
#Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación 
#R para residencias, I para industrias y C para comercios. 
#Calcule el precio a pagar de acuerdo con la siguiente tabla (Se encuentra en la plataforma)


#Declaracion de variables
R= "Residencias"
I= "Industrias"
C= "Comercios"

#Introduccion a la calculadora y declaracion de la variable "instalación" 
print("Calculadora de suministros de energia electronica")
print("Seleccione que tipo de instalacion utiliza: R para residencias. I para industrias o C para comercios")
instalacion= input("Seleccione la letra de su categoria: ")

#Proceso de la variable instalacion cuando es R
if instalacion == "R":
    a=int(input("Usted selecciono Residencia acontinuación introdusca la cantidad de kwh consumidos: "))
    if a<=500:
        print("Su deuda de la energia es de RD$550.00")
        print("Muchas gracias por utilizarnos")
    elif a>500:
        print("Su deuda de la energia es de RD$850.00")
        print("Muchas gracias por utilizarnos")

#Proceso de la variable instalacion cuando es I
if instalacion == "I":
    b=int(input("Usted selecciono Industria acontinuación introdusca la cantidad de kwh consumidos: "))
    if b<=1000:
        print("Su deuda de la energia es de RD$1300.00")
        print("Muchas gracias por utilizarnos")
    elif b>1000:
        print("Su deuda de la energia es de RD$2500.00")
        print("Muchas gracias por utilizarnos")

#Proceso de la variable instalacion cuando es C
if instalacion == "C":
    c=int(input("Usted selecciono Comercio acontinuación introdusca la cantidad de kwh consumidos: "))
    if c<=5000:
        print("Su deuda de la energia es de RD$3800.00")
        print("Muchas gracias por utilizarnos")
    elif c>5000:
        print("Su deuda de la energia es de RD$4200.00")
        print("Muchas gracias por utilizarnos")

#Proceso cuando la variable no coincide con ninguna variable dentro de la calculadora
if instalacion == "r":
    print("Caracter no indentificado porfavor escriba la letra en mayuscula.")

if instalacion == "i":
    print("Caracter no indentificado porfavor escriba la letra en mayuscula.")

if instalacion == "c":
    print("Caracter no indentificado porfavor escriba la letra en mayuscula.")

input()