from math import sqrt

n = int(input("Digite o número (n): "))


def loop_for():

    s = 0
    for x in range(1, n + 1):
        s += x/sqrt(x+2)

    print(s)


def loop_while():
    s = 0
    x = 1
    while x <= n:
        s += x/sqrt(x+2)
        x += 1

    print(s)


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
