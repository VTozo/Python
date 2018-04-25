
codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    classificacao = "Alimento não perecível"
elif 2 <= codigo <= 4:
    classificacao = "Alimento perecível"
elif 5 <= codigo <= 6:
    classificacao = "Vestuário"
elif codigo == 7:
    classificacao = "Higiene Pessoal"
elif 8 <= codigo <= 15:
    classificacao = "Alimento perecível"
else:
    classificacao = "Código inválido"

print(classificacao)
