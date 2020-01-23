def soma_elementos(lista):
    total = 0
    for i in lista:
        total = total + i
    return total

lista_soma = [2,3,4,5,8,7,9,10,23,45,100,-2,34]

print(soma_elementos(lista_soma))
