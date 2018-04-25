
n = int(input("Digite o valor máximo: "))


def loop_while():
    c = 1
    while c < n:
        print(c)
        c += 2
    return 1


def loop_for():
    for c in range(1, n, 2):
        print(c)
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()

