
def loop_while():
    n = 2
    while n < 100:
        if n % 4 == 0:
            print(n)
        n += 1
    return 1


def loop_for():

    for n in range(2, 99, 1):
        if n % 4 == 0:
            print(n)
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
