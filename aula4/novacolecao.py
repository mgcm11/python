def multiplicacao(mult):
    rs = 0
    for i in mult:
        rs+=i
    return mult 

def subtraçao(sub):
    rs = 0
    for i in sub:
        rs+=i
    return sub 

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)
    
