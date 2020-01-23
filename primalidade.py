def n_primos(x):
    



numero = int(input("Digite um número inteiro:"))

cont = 2
primo = True
 
while (cont < numero and primo):
 
    primo = not ((numero % cont) == 0)
    cont += 1
 
 
if (primo):
    print("primo")
else:
    print("não primo")