def cuenta_vocales(frase):
    cantidad_vocales = 0
    frase_modificada = frase.replace(" ", "").lower()
    for letra in frase_modificada:
        if letra == "a":
            cantidad_vocales += 1
        elif letra == "e":
            cantidad_vocales += 1
        elif letra == "i":
            cantidad_vocales += 1
        elif letra == "o":
            cantidad_vocales += 1
        elif letra == "u":
            cantidad_vocales += 1
    print("La cantidad de vocales de estra frase es: " , cantidad_vocales)

if __name__ == "__main__":
    frase_ingresada = input("Ingrese una frase: ")
    a = cuenta_vocales(frase_ingresada)
    print(a)

