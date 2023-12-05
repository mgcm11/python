def soma(numeros):
    """a funcao soma realiza a soma dos numeros
    que sao passados por parametros. e ao final, retorna
    o resultado da soma.
    Obs: Voce deve passar por parametros uma lista com numeros"""

    rs = 0
    for n in numeros:
        rs += n
    return rs 
# usando a funcao soma

v = [10,4,7,8,6]
print(soma(v))