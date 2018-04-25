
em_sequencia = False
count = 0
numeros = []

while not em_sequencia:
    x = int(input("Digite um número: "))

    numeros.append(x)

    if count >= 2 and numeros[count-2]+2 == numeros[count-1]+1 == numeros[count]:
        em_sequencia = True

    count += 1

print("Sequência digitada: %d, %d, %d" % (numeros[count-3], numeros[count-2], numeros[count-1]))
print("Média: ", (numeros[count-3] + numeros[count-2] + numeros[count-1])/3)
