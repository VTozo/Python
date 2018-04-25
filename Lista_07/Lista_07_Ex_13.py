
s = 0
count = 1
nivel_de_precisao = 51

for n in range(1, nivel_de_precisao, 2):
    if count % 2 == 0:
        s -= 1/(n ** 3)
    else:
        s += 1/(n ** 3)

    count += 1

pi = (32 * s) ** (1/3)

print("PI: ", pi)
