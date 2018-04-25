
numeros = []
impares = []
sair = False
count = 0

while not sair:

    x = int(input("Digite um número: "))
    numeros.append(x)
    if x % 2 == 1:
        impares.append(x)

    if numeros[count] == 0 and numeros[count-1] % 2 == 1:
        sair = True

    count += 1


print("Números: ", numeros)
print("Menor ímpar: ", min(impares))
