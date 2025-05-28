lista = [1, 1, 3, 5, 9, 8, 8, 4, 4]
def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos
print(elementos_unicos(lista))