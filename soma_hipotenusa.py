import math

def calc_hipotenusa(cat1,cat2):
    return math.sqrt(cat1**2 + cat2**2)

def e_hipotenusa(n):
    for cat1 in range(1, n):
        for cat2 in range(1, n):
            hip = calc_hipotenusa(cat1, cat2)
            if (hip == n):                
                return True
            else:
                continue

    return False    

def soma_hipotenusas(n):
    hipotenusas = []
    for i in range(1, n+1):
        if (e_hipotenusa(i)):
            hipotenusas.append(i)
        else: 
            continue

    return (sum(hipotenusas))

n = int(input("Digite um número: "))
print(soma_hipotenusas(n))