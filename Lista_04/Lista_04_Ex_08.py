salario = float(input("Digite seu salário: R$ "))
dependentes = int(input("Digite o número de dependentes: "))

if salario < 0 or dependentes < 0:
    print("O valor deve ser maior ou igual a zero!")
else:

    salario -= dependentes*189.59

    if salario <= 1903.98:
        imposto = 0.00
    elif salario <= 2826.65:
        imposto = (salario - 1903.98) * 0.075
    elif salario <= 3751.05:
        imposto = (2826.65 - 1903.98) * 0.075
        imposto += (salario - 2826.65) * 0.15
    elif salario <= 4664.68:
        imposto = (3751.05 - 2826.65) * 0.15
        imposto += (2826.65 - 1903.98) * 0.075
        imposto += (salario - 3751.05) * 0.225
    else:
        imposto = (2826.65 - 1903.98) * 0.075
        imposto += (3751.05 - 2826.65) * 0.15
        imposto += (4664.68 - 3751.05) * 0.225
        imposto += (salario - 4664.68) * 0.275

    print("O valor do imposto é: R$ %.2f" %imposto)
