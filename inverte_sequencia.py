def invert_list(lst):
    #lst.reverse()
    i = len(lst) - 1 
    while i >= 0:
        print (lst[i])
        i = i - 1

def main ():
    num = int(input("Digite um número: "))
    lista = []
    while num != 0:
        lista.append(num)
        num = int(input("Digite um número: "))
    invert_list (lista)


main()
