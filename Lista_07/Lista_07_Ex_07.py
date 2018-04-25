n = 1000

a = 1
b = 1

print("SEQUÊNCIA DE FIBONACCI:")

while b < n:
    print(a)
    a, b = b, a+b
print(a)
