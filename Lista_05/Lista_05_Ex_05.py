from random import choice


def f(n):
    return {
        1: "pedra",
        2: "papel",
        3: "tesoura"
    }[n]


print("JOQUEMPÔ")
print("1 = Pedra 2 = Papel 3 = Tesoura")

jogador = int(input())
cpu = choice([1, 2, 3])
print("Você jogou %s, e o cpu jogou %s..." % (f(jogador), f(cpu)))

if cpu == jogador:
    print("Empatou!")
elif (cpu == 1 and jogador == 3) or (cpu == 2 and jogador == 1) or (cpu == 3 and jogador == 2):
    print("Você perdeu...")
elif (jogador == 1 and cpu == 3) or (jogador == 2 and cpu == 1) or (jogador == 3 and cpu == 2):
    print("VOCÊ GANHOU!!!")
else:
    print("Valor inválido!")
