from random import choice

x = []
intervalo = [[], [], [], []]

for c in range(1, 101):
    n = choice(range(1, 101))
    x.append(n)

    if n <= 25:
        intervalo[0].append(n)
    elif n <= 50:
        intervalo[1].append(n)
    elif n <= 75:
        intervalo[2].append(n)
    elif n <= 100:
        intervalo[3].append(n)

print(len(intervalo[0]), ' números entre 01 e 25')
print(len(intervalo[1]), ' números entre 26 e 50')
print(len(intervalo[2]), ' números entre 51 e 75')
print(len(intervalo[3]), ' números entre 76 e 100')
