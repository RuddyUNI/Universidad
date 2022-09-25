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
variables= [a, b, c, d, e]

#Hacemos la lista de las palabras que ha escogido el usuario.
print("La lista que has creado es:", variables,)

#Ponemos un input para que el usuario escoga su palabra.
palabra= input("Escriba una palabra: ")
variables.count(palabra)

#Declaramos una variable para que printee cuantas veces se repite la palabra.
x= variables.count(palabra)
print("La palabra", palabra, "se repite", x, "veces")

#Ponemos que si la variable x es igual a 0 aparezca un texto que pone
#que la palabra introducida por el usuario no esta en la lista.
if x == 0:
    print("La palabra", palabra, "no esta en la lista.")

input()
