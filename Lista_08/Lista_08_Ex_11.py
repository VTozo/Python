
print("NÚMEROS PRIMOS")

for n in range(1, 501):

    divisores = 0

    for x in range(1, n+1):

        if n % x == 0:
            divisores += 1

    if divisores == 2:
        print(n)
