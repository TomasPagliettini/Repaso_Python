

def corroborar_step(numero):
    numero_str = str(numero)  # Convertimos a string para recorrer dígito por dígito
    numero_anterior = int(numero_str[0])  # Tomamos el primer dígito

    for a in numero_str[1:]:  # Recorremos desde el segundo dígito
        b = int(a)  # Convertimos el carácter a entero

        # Verificar que la diferencia sea exactamente 1
        if abs(b - numero_anterior) != 1:
            return False  # Si no cumple, no es un número step

        numero_anterior = b  # Actualizar el número anterior para la siguiente iteración

    return True  # Si recorrió todo sin problemas, es un número step


numero_ingresado = int(input("Ingrese un número: "))
a = corroborar_step(numero_ingresado)
print(a)
