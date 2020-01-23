lista1=["vermelho","verde","azul"]
lista2=lista1
#a lista 2 passa a se referenciar a lista 1

lista2[0]="rosa""
#alterando a lista2,a lista 1 tb será alterada, pq ambas as variaveis estao se referindo a mesma lista. Nao se cria uma nova lista
#ambas as variaveis estao se referindo a mesma lista. Alterando uma altera ambas.

#CLONAGEM DE LISTA:
def clone(lista):
    clone = []
    for objeto in  lista:
        clone.append(objeto)
    
    return clone

    # será devolvida uma nova lista armazenada em outro lugar da memoria
    # clonando a lista 2, conseguirá alterar apenas os elementos da lista 2

    #obs: fatiamentos que criam nova lista:
        lista1[ini:fim]
        lista1[ini:]
        lista1[:fim]
        lista1[:] #devolve um clone da lista, logo a funçao clone nao é muito utilizada, basta realizar tal procedimento mais simples
            #ex:lista2 = lista1[:] - ja cria uma clone da lista 1
    

#PERTINENCIA A UMA LISTA
    ex: rosa in lista1 # retorna True ou False para saber se um elemento esta contido em uma lista

#CONCATENAÇAO DE LISTAS:
    exe: [1,2] + [3,4] = [1,2,3,4]

    append = acrescenta um item ao final da lista.Altera uma lista existente
    concatenaçao = nao altera lista existente. cria-se uma nova lista sem alterar as listas existentes

#REPETIÇAO DE LISTAS:
    ex: a = [1,2,3]
        a_trip = a * 3 # nao é uma multiplicaçao numerica, na vdd pega a lista e repete 3 vezes como pedido
        a_trip = [1,2,3,1,2,3,1,2,3]

#REMOÇAO DE ELEMENTOS EM LISTAS:
    ex: a = [1,2,3]
        del a[1] # apagará o elemento um da lista (removerá o 2)



