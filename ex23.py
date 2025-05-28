nomes = ['Alec', 'Alec', 'Felipe', 'Felipe', 'Alline', 'Alline', 'Ana','Alec']
def nomes_duplicado(nomes):
    duplicados = []
    for item in nomes:
        if item not in duplicados:
            duplicados.append(item)
    return duplicados
print(nomes_duplicado(nomes))
