def prime(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if  x % fator == 0:
        return False
    else:
        return True


def n_primos(limite):
    n = 2
    i = 0
    while n <= limite:
        if prime(n):
            i+=1    
        n = n + 1

    return i