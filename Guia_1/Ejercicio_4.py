numeros_lista = [8,12,9,45]
def orden (lista):
    lista.sort(reverse = True)
    return lista

print("Lista sin ordenar", numeros_lista)
numeros_ordenados = orden(numeros_lista)
print(numeros_ordenados)