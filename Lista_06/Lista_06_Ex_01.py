

def loop_while():
    n = 1
    while n < 100:
        print(n)
        n += 2
    return 1


def loop_for():
    for n in range(1, 100, 2):
        print(n)
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
