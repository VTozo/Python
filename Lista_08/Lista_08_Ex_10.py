from time import sleep

for s in range(600, -1, -1):
    minutos = s//60
    segundos = s % 60
    print('%02d:%02d' % (minutos, segundos))
    sleep(1)
