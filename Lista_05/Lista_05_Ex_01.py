
massa = float(input("Digite a massa em Kg: "))
massa_libras = massa * 2.20462262

print("Massa em Libras: %.2f" %massa_libras)

if massa_libras >= 201:
    print("Categoria: Peso-pesado")
elif massa_libras >= 176:
    print("Categoria: Cruzador")
elif massa_libras >= 169:
    print("Categoria: Meio-pesado")
elif massa_libras >= 161:
    print("Categoria: Super-médio")
else:
    print("Categoria: inferior a super-médio")
