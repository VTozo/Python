a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Os valores devem ser maiores que zero!")
elif(a > b+c) or (b > a+c) or (c > a+b):
    print("Não forma triângulo!")
elif a == b and b == c:
    print("O triângulo é equilátero")
elif a == b or a == c or b == c:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
