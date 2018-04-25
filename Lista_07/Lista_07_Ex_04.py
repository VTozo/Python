
v = []
impares = []

for c in range(0, 10):
    x = int(input("Digite o " + str(c+1) + "º número: "))
    v.append(x)

for c in v:
    if c % 2 == 1:
        impares.append(c)

print("A média dos números ímpares é: ", sum(impares)/len(impares))
