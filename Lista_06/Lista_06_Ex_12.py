t = int(input("Digite uma temperatura em graus Celsius: "))


def loop_for():

    for c in range(t-10, t+11):
        f = c * 1.8 + 32
        print("%.dº Celsius = %.dº Farenheit" % (c, f))


def loop_while():
    c = t - 10
    while c <= t + 10:
        f = c * 1.8 + 32
        print("%.dº Celsius = %.dº Farenheit" % (c, f))
        c += 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
