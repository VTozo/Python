n = int(input("Digite o número de termos: "))

a = 1
b = 1
count = 1

print("SEQUÊNCIA DE FIBONACCI:")

while count < n:
    print(a)
    a, b = b, a+b
    count += 1
print(a)
