from functools import reduce

def minha_multiplicacao(*args):
    numeros = [n for n in args if isinstance(n, (int, float))]
    if not numeros:
        return 1
    return reduce(lambda x, y: x * y, numeros)

print(minha_multiplicacao(1, 2, 3, "a", [4], 5.0, True))