
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

if x == 0 or y == 0:
    print("O ponto não está em nenhum quadrante!")
elif 0 < x and 0 < y:
    print("O ponto está no 1² quadrante")
elif y < 0 < x:
    print("O ponto está no 2² quadrante")
elif x < 0 and y < 0:
    print("O ponto está no 3² quadrante")
elif x < 0 < y:
    print("O ponto está no 4² quadrante")
else:
    print("ERROR!")
