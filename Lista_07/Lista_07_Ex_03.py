n = int(input("Digite o número de termos: "))
v = []

for c in range(0, n):
    x = int(input("Digite o " + str(c+1) + "º número: "))
    v.append(x)

maior = v[0]
menor = v[0]

for c in v:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c

print("Maior: ", maior)
print("Menor: ", menor)
