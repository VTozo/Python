

def loop_while():
    p = 1
    while p <= 20:
        c = p * 2.54
        print("%.2f polegadas = %.2f centimetros" % (p, c))
        p += 1
    return 1


def loop_for():
    for p in range(1, 21):
        c = p * 2.54
        print("%.2f polegadas = %.2f centimetros" % (p, c))
    return 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
