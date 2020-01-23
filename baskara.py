import math

def delta(a,b,c):
    return b ** 2 - 4 * a * c

def main():    
    numero1= float(input("Entre com um valor para A: "))
    numero2 = float(input("Entre com um valor para B: "))
    numero3 = float(input("Entre com um valor para C: "))
    imprime_raizes(numero1,numero2,numero3)

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if d == 0:
        raiz1 = (-b + math.sqrt(delta(a,b,c))) / (2 * a)
        print ("A única raiz é: ", raiz1)

    else:
        if d < 0:
            print ("Essa equação  não possui  raízes reais.")
        else:
            raiz1 = (-b + math.sqrt(d))) / (2 * a)
            raiz2 = (-b - math.sqrt(d))) / (2 * a)
            print ("A primeira raíz é: ")
            print("A segunda raíz é: ")
            