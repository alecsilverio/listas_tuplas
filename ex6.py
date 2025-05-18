numeros = []
for i in range(5):
    numero = int(input(f'Digite um número:'))
    numeros.append(numero)

print(f'O maior número é: {max(map(int, numeros))}')