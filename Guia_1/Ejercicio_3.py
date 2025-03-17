ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))
caracter_a_usar = input("Ingrese el caracter con el que se va a rellenar el rectangulo: ")

for a in range(alto):
    print((caracter_a_usar + " ")*ancho)
    
