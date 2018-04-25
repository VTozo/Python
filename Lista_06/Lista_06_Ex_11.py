print("PROGRESSÃO ARITMÉTICA")

a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
n = int(input("Digite o número de termos: "))


def loop_while():
    x = 1
    while x <= n:
        a = a1 + (x - 1) * r
        print(a)
        x += 1
    return 1


def loop_for():
    for x in range(1, n+1):
        a = a1 + (x - 1) * r
        print(a)
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
