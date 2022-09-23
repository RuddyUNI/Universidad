#Ruddy Contreras 21-1826 - Tema: Veces que se repite una palabra

#Escriba un programa que permita crear una lista de palabras y que, 
#a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.



#Ponemos algunos input para que se declaren las variables que el usuario quiera.
print("Escriba 5 palabras para crear la lista")
a= input("Escriba la primera palabra: ")
b= input("Escriba la segunda palabra: ")
c= input("Escriba la tercera palabra: ")
d= input("Escriba la cuarta palabra: ")
e= input("Escriba la quinta palabra: ")

#Juntamos todas las variables en una sola.
variables= a, b, c, d, e

#Hacemos la lista de las palabras que ha escogido el usuario.
print("La lista que has creado es:", variables,)

#Ponemos un input para que el usuario escoga su palabra.
palabra= input("Escriba una palabra: ")

#Ponemos en cada variable que sume 1 numero si la palabra se parece y en caso contrario ponga un 0.
if palabra == a:
    a1= 1
elif palabra != a:
    a1=0

if palabra == b:
    b1= 1
elif palabra != b:
    b1= 0

if palabra == c:
    c1= 1
elif palabra != c:
    c1=0

if palabra == d:
    d1= 1
elif palabra != d:
    d1=0

if palabra == e:
    e1= 1
elif palabra != e:
    e1=0

#Sumamos cada variable para saber el total de veces que se repite la misma variable.
resultado= (a1 + b1 + c1 + d1 + e1)
print("La palabra", palabra, "se repite", resultado, "veces")

#Ponemos que si la palabra que escoge el usuario no se parece a ninguna variable
#ponga que la palabra introducida no esta en la lista.
if palabra != a != b != c != d != e:
    print("La palabra", palabra, "no esta en su lista.")


input()
