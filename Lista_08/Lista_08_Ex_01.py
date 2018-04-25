
numeros = []
n_fornecidos = 0
zero = False
total = 0
pares = 0
impares = 0

while not zero:
    x = int(input("Digite um número: "))

    if x == 0:
        zero = True
    else:
        numeros.append(x)
        n_fornecidos += 1

print("Números fornecidos: ", n_fornecidos)

for n in numeros:
    if n % 2 == 0:
        total += n
        pares += 1
    else:
        total -= n
        impares += 1

print("Total: ", total)
print("Pares: ", (pares/n_fornecidos)*100, "%")
print("Ímpares: ", (impares/n_fornecidos)*100, "%")
