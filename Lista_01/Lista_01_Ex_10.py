import math

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

area_base = 3.14*raio**2
area_lateral = 2 * 3.14 * raio * altura
area_total = area_base + area_lateral

latas = math.ceil(area_total/15)
preco = latas * 50

print("O preço fica: $", preco, ",00")