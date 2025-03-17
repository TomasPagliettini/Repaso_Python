import math
def corroborar_numero_step(numero_ingresado):
    numero_ingresado  = str(numero_ingresado)
    numero_modificado = numero_ingresado.replace(" ", "")
    bandera = True
    numero_modificado_entero = int(numero_modificado)
    primer_digito = numero_modificado_entero // 10**(math.floor(math.log10(numero_modificado_entero)))
    digito_anterior = primer_digito
    for a in numero_modificado:
        a = int(a)
        
        if a + 1 == digito_anterior or a - 1 == digito_anterior:
            digito_anterior = a
            
        else:
            bandera = False
            break
    if bandera:
        print("Este numero es step")

    else:
        print("Este numero no es step")
        



a = input("Ingrese un numero: ")
corroborar_numero_step(a)
