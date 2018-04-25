idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você não pode votar")
elif 16 <= idade < 18 or idade >= 65:
    print("O voto é facultativo")
else:
    print("O voto é obrigatório")
