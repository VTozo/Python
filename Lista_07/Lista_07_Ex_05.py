
pares = []
while len(pares) < 3:
    x = int(input("Digite um número: "))
    if x % 2 == 0:
        pares.append(x)

maior = pares[0]
for n in pares:
    if n > maior:
        maior = n

print("O maior número par é: ", maior)
