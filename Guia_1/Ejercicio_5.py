
def corroborar_palidromo(palabra_a_analizar):
    palabra_modificada =  palabra_a_analizar.lower() 
    if palabra_modificada == palabra_modificada[::-1]:
        return "Esta palabra es palidroma"
    else:
        return "Esta palabra no es palidroma"

palabra_ingresada = input("Ingrese una palabra PALINDROMA: ")
a = corroborar_palidromo(palabra_ingresada)
print(a)
