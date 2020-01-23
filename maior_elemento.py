def maior_elemento(lista):
    maior_el = 0 
    for i in lista:
        if i > maior_el:
            maior_el = i
    
    return maior_el

lista_num= [6,7,8,9,3,4,56,99,1000,-2,4,5]

print(maior_elemento(lista_num))
        
        
