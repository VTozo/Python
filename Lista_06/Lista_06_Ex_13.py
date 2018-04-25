print("N-ÉSIMO NÚMERO HARMÔNICO")

n = int(input("Digite o número (n): "))


def loop_for():
    h = 0
    for x in range(1, n+1):
        h += 1/x

    print(h)


def loop_while():
    h = 0
    x = 1
    while x <= n:
        h += 1/x
        x += 1
    print(h)


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()

