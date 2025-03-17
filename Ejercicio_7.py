def corroborar_numero_step(numero_ingresado):
    numero_ingresado  = str(numero_ingresado)
    numero_modificado = numero_ingresado.replace(" ", "")
    #numero_modificado = int(numero_modificado)
    bandera = True
    numero_anterior = 0
    for a in numero_modificado:
        #numero_modificado = int(numero_modificado)
        a = int(a)
        
        if a + 1 == numero_anterior or a - 1 == numero_anterior:
            numero_anterior = a
            
        else:
            bandera = False
            break
    if bandera:
        print("Este numero es step")

    else:
        print("Este numero no es step")
        



a = input("Ingrese un numero: ")
corroborar_numero_step(a)
