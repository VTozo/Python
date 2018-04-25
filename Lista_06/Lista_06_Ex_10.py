
li = int(input("Digite o limite inicial: "))
lf = int(input("Digite o limite final: "))

if li > lf:
    print("O limite inicial deve ser menor que o limite final!")
    exit()

print("MÚLTIPLOS DE TRÊS:")


def loop_for():

    for n in range(li+1,lf):
        if n % 3 == 0:
            print(n)


def loop_while():

    n = li + 1
    while n < lf:
        if n % 3 == 0:
            print(n)
        n += 1


print("----------Usando WHILE:----------")
loop_while()
print("----------Usando FOR:----------")
loop_for()
