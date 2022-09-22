valores = input().split()

tempo = int(valores[0])
velMed = int(valores[1])
comsumo = 12

dist = velMed*tempo
comb = dist/comsumo

print("{:.3f}".format(comb))