
def loop_while():
    n = -100
    while n <= 100:
        print(n)
        n += 10
    return 1


def loop_for():

    for n in range(-100, 101, 10):
        print(n)
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
