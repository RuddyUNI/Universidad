#Ruddy Contreras 21-1826 - Tema: Números de lotería

#Escriba un programa que pregunte al usuario los números de su ticket de lotería, 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 


#Le pedimos al usuario sus 5 tickets de lotería.
numero1 = int(input("¿Cual es su primer ticket de lotería? "))
numero2 = int(input("¿Cual es su segundo ticket de lotería? "))
numero3 = int(input("¿Cual es su tercer ticket de lotería? "))
numero4 = int(input("¿Cual es su cuarto ticket de lotería? "))
numero5 = int(input("¿Cual es su quinto ticket de lotería? "))

#Creamos una variable con todas las otras juntas.
tickets= [numero1, numero2, numero3, numero4, numero5]

#Printeamos la lista con la nueva variable creada.
print("La lista de sus tickets es:", tickets)

#La ordenamos de menor a mayor
ordenados= sorted(tickets)
print("La lista de tickers ordenados de menor a mayor:", ordenados)


input()