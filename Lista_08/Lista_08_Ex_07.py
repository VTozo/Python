
notas = []

for c in range(1, 7):
    x = int(input('Digite a %dª nota: ' % c))
    notas.append(x)

notas.remove(max(notas))
notas.remove(min(notas))

print('Nota final: ', sum(notas)/len(notas))
