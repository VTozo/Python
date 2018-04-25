
numeros = []
em_sequencia = False
count = 0

while not em_sequencia:
    x = int(input("Digite um número: "))
    numeros.append(x)

    if count >= 2 and numeros[count] == numeros[count-1]:
        em_sequencia = True
        numeros.pop()
        numeros.pop()

    count += 1


print("Números: ", numeros)
print("Média: ", sum(numeros)/len(numeros))
