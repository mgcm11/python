lista = [30,8,60,4]

dic = {1:10,2:30,3:50}

def soma(valores):
    rs = 0
    for i in valores:
        rs+=i
    print(rs)
    
def soma2(*valores):
    a,b,c,d = valores
    rs = a+b+c+d
    print(rs)

def soma3(**num):
        a,b,c, = num
        rs = num[a]+num[b]+num[c]
        print(rs)

soma(lista)
soma2(*lista)
soma3(**dic)