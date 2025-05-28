numeros = []
for _ in range(11):
    num = int(input('Digite um número: '))
    numeros.append(num)

for num in numeros[:]:
    if num % 2 == 0:
        numeros.remove(num)

print(numeros)