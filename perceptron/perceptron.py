

def soma(e, p):
    s = 0
    for i in range(len(e)):
        s = s + e[i]*p[i]
    return s

def stepFunction(soma):
    if(soma>=1):
        return 1
    return 0

entradas = [1 , 7 , 5]
pesos = [0.8, 0.1, 0]

s = soma(entradas, pesos)

r = stepFunction(s)