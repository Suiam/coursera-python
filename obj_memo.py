#OBJETOS E REFERENCIAS:
a= "banana"
# a é como se fosse um apontador de memoria para verificar onde esta armazenado

b="banana""
# tanto a quanto b apontaram para a mesma parte da memoria referente a banana.
# em python string sao imutaveis

c="maça"

a is b # o comando is diz se ambas as referencias apontam para o mesmo objeto. No caso será true

no caso de listas, que sao mutaveis:
a=[81,82,83]
b=[81,82,83]
# nesse caso armazena em locais diferentes, apesar de mesmo conteudo
a is b # nesse caso será False pois sao objetos diferentes
a == b # será true pois o conteudo é identico

#REPETIÇOES E REFERENCIAS:
    ex: list = [45,76,34,55]
        list*3 = [45,76,34,5,45,76,34,5,45,76,34,5]
        [list] * 3 = [[45,76,34,5], [45,76,34,5], [45,76,34,5]]
            #criou-se listas de listas
       
        newlist = [[45,76,34,5], [45,76,34,5], [45,76,34,5]]
        list = [45,76,34,55]
        list[1] = 99
        list = [45,99,34,55]
        newlist = [[45,99,34,5], [45,99,34,5], [45,99,34,5]]
        # onde estava o 76 será alterado em ambas as listas.
        
    
