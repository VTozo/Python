
for n in range(1, 100):

    n = int(input("Digite um número: "))  # COMENTE ESSA LINHA PARA TESTAR TODOS OS VALORES
    r = ""  # VARIÁVEL PARA O RESULTADO

    if not 1 <= n <= 99:  # SE NÃO ESTIVER ENTRE 1 E 99
        print("Entrada fora dos limites operacionais!")
        exit()


    def unidade(u):
        return {
            1: "um",
            2: "dois",
            3: "três",
            4: "quatro",
            5: "cinco",
            6: "seis",
            7: "sete",
            8: "oito",
            9: "nove"
        }[u]


    def dezena(u):
        return {
            2: "vinte",
            3: "trinta",
            4: "quarenta",
            5: "cinquenta",
            6: "sessenta",
            7: "setenta",
            8: "oitenta",
            9: "noventa"
        }[u]


    def dez_a_19(u):
        return {
            10: "dez",
            11: "onze",
            12: "doze",
            13: "treze",
            14: "quatorze",
            15: "quinze",
            16: "dezesseis",
            17: "dezessete",
            18: "dezoito",
            19: "dezenove"
        }[u]


    if 1 <= n <= 9:
        r = unidade(n).capitalize()
    elif 10 <= n <= 19:
        r = dez_a_19(n).capitalize()
    elif str(n)[1] == "0":
        d = int(str(n)[0])
        r = dezena(d).capitalize()
    else:
        d = int(str(n)[0])
        e = int(str(n)[1])
        r = (dezena(d)+" e "+unidade(e)).capitalize()

    print(r)
