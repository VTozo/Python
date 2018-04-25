def loop_while():
    n = 20000
    while n <= 160000:
        m = n * 1609.344
        print("%.2f metros = %.2f milhas" % (n, m))
        n += 10000
    return 1


def loop_for():
    for n in range(20000, 160001, 10000):
        m = n * 1609.344
        print("%.2f metros = %.2f milhas" % (n, m))
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
