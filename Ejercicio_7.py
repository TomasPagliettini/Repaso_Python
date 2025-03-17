import math
def corroborar_numero_step(numero_ingresado):
    numero_modificado = int(str(numero_ingresado).replace(" ", ""))
    bandera = True
    primer_digito = numero_modificado // 10**(math.floor(math.log10(numero_modificado)))
    numero_modificado_str = str(numero_modificado)
    digito_anterior = int(numero_modificado_str[0])
    for a in range(1, len(numero_modificado_str)):
        valor_actual = int(numero_modificado_str[a]) 
        
        if valor_actual + 1 == digito_anterior or valor_actual - 1 == digito_anterior:
            digito_anterior = valor_actual
            
        else:
            bandera = False
            break
    if bandera:
        print("Este numero es step")

    else:
        print("Este numero no es step")
        



a = input("Ingrese un numero: ")
corroborar_numero_step(a)


