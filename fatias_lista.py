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



limite = int(input("Limite máximo: "))

n = 2

while n < limite:
    if eh_primo(n):
        print(n, end = ", ")
    
    n = n + 1


primos[1:2] #pega os valores que começam no indice um e um a menos que o dois
primos[2:7] # devolve os elementos a partir da posiçao 2 até a posiçao 6 (7-1)
primos[:12] # devolve os elementos do inicio (0) até a posiçao 12 -1, ou seja, 11
primos[12:] # devolve os elementos a partir da posiçao 12 até o final da lista



