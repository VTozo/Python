n = int(input("Digite o número de termos: "))

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
count = 1

print("SEQUÊNCIA DE FETUCCINE:")

print(a)

while count < n:
    print(b)
    if count % 2 == 0:
        a, b = b, b-a
    else:
        a, b = b, a+b

    count += 1

