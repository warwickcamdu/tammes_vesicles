matrix = []

k1 = 13.6734305954591
k2 = -1.55506734709777
k3 = -0.345863281437394

line = []
line.append("-")
for prot in range(1, 51):
    line.append(prot)
matrix.append(line)

for ves in range(1, 51):
    line = []
    line.append(ves)

    for prot in range(1, 51):
        floatves = float(ves)
        ratio = float(floatves / prot)
        pred = round(k1 * ratio * ratio + k2 * ratio + k3)
        line.append(pred)
    matrix.append(line)

import csv
with open('matrix.csv', "wb") as f:
    writer = csv.writer(f)
    writer.writerows(matrix)
