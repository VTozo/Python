
s = 0
n = int(input("Digite o número do fim da sequência: "))

for count in range(1, n+1):

    s += (2*count-1)/(3*count)

print(s)
