import datetime
now = datetime.datetime.now()
ano_atual = now.year
ano = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano
print("Neste ano você fez/fará ", idade, " anos")
