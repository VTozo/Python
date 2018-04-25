
x = []
"""
for n in range(1, 11):
    x.append(int(input("Digite o %.dº número: " % n)))
"""

n = 1
while n <= 10:
    x.append(int(input("Digite o %.dº número: " % n)))
    n += 1

soma = sum(x)
media = soma/len(x)

print("Soma = ", soma)
print("Média = ", media)
