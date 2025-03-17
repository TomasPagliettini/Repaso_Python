numeros_lista = [8,12,9,45]
def orden (lista):
    lista.sort(reverse = True)
    return f"Lista ordenada: {lista}"



if __name__ == "__main__":
    print("Lista sin ordenar", numeros_lista)
    numeros_ordenados = orden(numeros_lista)
    print(numeros_ordenados)