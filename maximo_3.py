def maximo(a,b,c):
    if (a==b and a==c ) or (b==a and b==c) or (c==a and c==b):
        return a
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c> b:
        return c 

numero1= int(input("Entre com um número: "))
numero2= int(input("Entre com um segundo número: "))
numero3= int(input("Entre com um terceiro número: "))

print (maximo(numero1,numero2,numero3))
