n = int(input("Digite o número de termos: "))

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
count = 1

print("SEQUÊNCIA DE RICCI:")

while count < n:
    print(a)
    a, b = b, a+b
    count += 1
print(a)
