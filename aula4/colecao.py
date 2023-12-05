def soma(valores):
    """soma, realiza a soma dos valores que estao 
    em uma lista retorna o resultado da soma"""
    rs = 0 
    for i in valores:
        rs+=i
    return rs

def media(valores):
    """a funcao media realiza a soma dos valores e divede pela quantidade de valores somados
    e retorna o resultado"""
    rs = 0 
    qtd = len(valores)
    for i in valores:
        rs+=i 
    return rs/qtd

def maior(valores):
    """a funçao maior retorna o maior valor de uma lista"""
    m = valores[0]
    for i in valores:
        if i > m:
            m = i
    return m 


def menor(valores):
    """a funçao menor retorna o menor valor de uma lista """
    m = valores[0]
    for i in valores:
        if i < m:
            m = i
    return m 

