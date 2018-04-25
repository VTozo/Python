
preco = float(input("Digite o preço do produto: R$ "))

print("1 - À vista")
print("2 - Em 2 parcelas")
print("3 - Em 3 parcelas")
print("4 - Em 4 parcelas")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    valor_final = preco * 0.92
    print("O valor é: R$ %.2f" %valor_final)
elif opcao == 2:
    valor_final = preco * 0.96 / 2
    print("O valor é: 2 vezes de R$ %.2f" %valor_final)
elif opcao == 3:
    valor_final = preco / 3
    print("O valor é: 3 vezes de R$ %.2f" %valor_final)
elif opcao == 4:
    valor_final = preco * 1.04 / 4
    print("O valor é: 4 vezes de R$ %.2f" %valor_final)
else:
    print("Opção inválida!")
