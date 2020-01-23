def eh_primo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0  and fator <= x/2:
        fator = fator + 1
    if  x % fator == 0:
        return False
    else:
        return True



limite = int(input("Digite um número: "))

n = 2

while n < limite:
    if eh_primo(n):
        print(n, end = ", ")
    
    n = n + 1
