massa = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = massa/(altura**2)

print("o seu IMC é: %.2f" % imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Acima do peso")
else:
    print("Obeso")

