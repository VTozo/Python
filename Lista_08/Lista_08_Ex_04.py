
numeros = []
count = 0
final = False

while not final:
    x = int(input("Digite um número: "))
    numeros.append(x)
    if numeros[0] == numeros[count] and count > 0:
        final = True
    count += 1

numeros.pop(0)
numeros.pop()

print("Números: ", numeros)
print("Soma: ", sum(numeros))
