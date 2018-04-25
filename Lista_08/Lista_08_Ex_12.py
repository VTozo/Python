
print("NÚMEROS PERFEITOS")

for n in range(1, 10001):

    divisores = []

    for x in range(1, n):

        if n % x == 0:
            divisores.append(x)

    if sum(divisores) == n:
        print(n)
