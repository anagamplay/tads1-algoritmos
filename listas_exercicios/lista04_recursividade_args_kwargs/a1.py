from functools import reduce

def minha_soma(*numeros):
    return reduce(lambda x, y: x + y, numeros)

print(minha_soma(1,2,3,4,5,6))