import re

def le_assinatura():
  #'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]
    
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def le_textos2():
    return [ r"""Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.""",
             r"""Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres. """, 
             r"""NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."""]

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_medio_palavra(palavras):
    numero_de_palavras = len(palavras)
    tamanho_da_palavra = 0
    for p in palavras:
        tamanho_da_palavra += len(p)

    return tamanho_da_palavra / numero_de_palavras

def type_token(palavras):
    diferentes = n_palavras_diferentes(palavras) 
    total = len(palavras)
    return diferentes / total

def hapax(palavras):
    unicas = n_palavras_unicas(palavras)
    total = len(palavras)
    return unicas / total

def tamanho_medio_da_sentenca(sentencas):
    n_caract_todas_sentencas = 0
    for s in sentencas:
        n_caract_todas_sentencas += len(s)  

    numero_de_sentencas = len(sentencas)

    return n_caract_todas_sentencas / numero_de_sentencas
        
def complexidade_da_sentenca(sentencas):
    numero_de_sentencas = len(sentencas)
    total_de_frases = 0
    for s in sentencas:        
        frases = separa_frases(s)
        total_de_frases += len(frases)
    return total_de_frases / numero_de_sentencas

def tamanho_medio_da_frase(frases):
    numero_de_frases = len(frases)
    total_de_chars = 0
    for f in frases:
        numero_de_chars = len(f)
        total_de_chars += numero_de_chars

    return total_de_chars / numero_de_frases


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    total = 0
    for i in range(6):
        total += abs(as_a[i] - as_b[i])

    return total / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    frases = []
    palavras = []
    sentencas = separa_sentencas(texto)
    for s in sentencas: 
        frases += separa_frases(s)
        for f in frases:
            palavras += separa_palavras(f)

    wal = tamanho_medio_palavra(palavras)
    ttr = type_token(palavras)
    hlr = hapax(palavras)
    sal = tamanho_medio_da_sentenca(sentencas)
    sac = complexidade_da_sentenca(sentencas)
    pal = tamanho_medio_da_frase(frases)
    
    return [wal, ttr, hlr, sal, sac, pal]



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
 
    ass = []
    for t in textos:
        assinatura = calcula_assinatura(t)
        ass += [compara_assinatura(assinatura, ass_cp)]

    return ass.index(min(ass)) + 1

ass_cp = le_assinatura()
textos = le_textos()
resultado = avalia_textos(textos, ass_cp)
print("O autor do texto", resultado,  "está infectado com COH-PIAH")