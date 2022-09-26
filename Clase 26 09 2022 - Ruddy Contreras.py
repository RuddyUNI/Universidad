#Escriba un programa que imprima la tabla de multiplicar de un numero con la entrada de teclado


num1= int(input("Seleccione un numero para hacer la tabla: "))
num2= 1

while num2 <= 20: 
    print(str(num1), "*", (str(num2)), "=", num1*num2)
    num2=(num2+1)


input()
