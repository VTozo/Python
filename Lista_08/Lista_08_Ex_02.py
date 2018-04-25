
numeros = []
cinco_validos = False

while not cinco_validos:
    x = int(input("Digite um número: "))

    if x % 3 != 0:
        numeros.append(x)
    if len(numeros) == 5:
        cinco_validos = True

print("Números válidos: ", numeros)
print("Média: ", sum(numeros)/len(numeros))
