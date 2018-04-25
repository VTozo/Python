
print("1- Dólar 2- Libra- 3 Euro")
moeda = int(input("Qual moeda você quer? "))

if moeda < 1 or 3 < moeda:
    print("Valor incorreto!")
    exit()

montante = float(input("Digite o valor desejado: "))
if montante < 0:
    print("Valor incorreto!")
    exit()

if moeda == 1:
    preco = montante * 3.30152861
elif moeda == 2:
    preco = montante * 4.65882003
elif moeda == 3:
    preco = montante * 4.06302618

if montante < 1000:
    preco *= 1.05
else:
    preco *= 1.03

print("O preço final é: R$ %.2f" %preco)
