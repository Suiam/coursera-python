def desenha(linha):    
    while linha > 0:
        coluna = 1
        while coluna <= linha:
            print('*', end = "")
            coluna = coluna + 1
        print()
        linha = linha - 1


linha = int(inpu("digite a largura: "))
