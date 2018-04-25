
def loop_while():
    n = 50
    while n >= 0:
        print(n)
        n -= 5
    return 1


def loop_for():

    for n in range(50, -1, -5):
        print(n)
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
