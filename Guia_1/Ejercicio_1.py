lista = [8,12,9,45]
posicion = 0
num_encontrado = False
valor_ingresado = input("ingrese un valor de la lista [8,12,9,45]: ")
valor_ingresado_numero = int(valor_ingresado)
for elemento in lista:
    
    if elemento == valor_ingresado_numero:
        num_encontrado = True
        print("El  numero se encuentra en la posicion ", posicion)
    posicion += 1
if num_encontrado == False:
        print("El numero no esta en la lista")
        breakpoint
    


