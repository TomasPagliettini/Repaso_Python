lista = [8,12,9,45]
posicion = -1
num_encontrado = 0
valor_ingresado = input("ingrese un valor de la lista [8,12,9,45]: ")
valor_ingresado_numero = int(valor_ingresado)
for elemento in lista:
    posicion += 1
    if elemento == valor_ingresado_numero:
        num_encontrado = 1
        print("El  numero se encuentra en la posicion ", posicion)
if not num_encontrado:
        print("El numero no esta en la lista")
        breakpoint
    


