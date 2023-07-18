import os

os.system('cls') or None 

while True:
    valIni = input("digite o valor inicial: ")
    valIni = int(valIni)
    if valIni >= 0:
        break

print()

while True:
    valFin = input("digite o valor final: ")
    valFin = int(valFin)
    if valFin >= 0:
        break

print()

DifVal = valFin - valIni
Perc = (abs(DifVal) / valIni) * 100

if DifVal < 0:
    print('A variação percentual foi de - ', Perc, "%")

else:
    print('A variação percentual foi de + ', Perc, "%")


