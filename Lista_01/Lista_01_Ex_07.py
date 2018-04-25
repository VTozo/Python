
hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

total_minutos = hora*60+minutos
total_segundos = hora*3600+minutos*60+segundos

print("Já se passaram ", total_minutos, " minutos desde o inicio do dia")
print("Já se passaram ", total_segundos, " segundos desde o inicio do dia")
