def eh_primo(num):
    i = 2
    while (i*i <= num):
        if (num % i==0):
            return False
        i += 1
    return True

def maior_primo(num):
    i = num
    while (i >= 2):
        if eh_primo(i):
            return i
        i = i - 1

numero = int(input("Digite um número:"))

print (maior_primo(numero))
         
            
            
