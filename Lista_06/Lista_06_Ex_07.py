# Função Babbage: f(x) = x² + x + 41


def loop_while():
    x = 1
    while x <= 20:
        c = x*x + x + 41
        print(c)
        x += 1
    return 1


def loop_for():
    for x in range(1, 21):
        c = x*x + x + 41
        print(c)
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
