
s = 0

for count in range(1, 11):
    if count % 2 == 0:
        s -= count/(count*count)
    else:
        s += count/(count*count)
print(s)
