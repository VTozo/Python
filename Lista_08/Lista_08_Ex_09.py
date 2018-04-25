
for c in range(1, 11):
    x = int(input('Digite o %dº número: ' % c))

    if x == 0:
        print('Não atendido pelo programa.')
    elif x > 0:
        for n in range(x, -1, -1):
            print(n, end=' ')
        print()
    else:
        for n in range(x, 1):
            print(n, end=' ')
        print()
