x1 = float(input("Entre com um número inteiro: "))
y1 = float(input("Entre com um número inteiro: "))
x2 = float(input("Entre com um número inteiro: "))
y2 = float(input("Entre com um número inteiro: "))

import math

distancia = (x2 - x1) ** 2 + (y2 - y1) ** 2
distancia = math.sqrt(distancia)

if distancia >= 10:
    print("longe")
else:
    print("perto")     
