n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))
r = 0

while n1 >= n2:
    r += 1
    n1 -= n2

print("n1 // n2 = ", r)
print("Resto = ", n1)
