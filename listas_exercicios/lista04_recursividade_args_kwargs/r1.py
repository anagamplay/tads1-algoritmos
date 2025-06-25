n = int(input('Insira um número inteiro: '))

def contagem_regressiva(n):
    print(n)
    if n == 0:
        return print('Boom!')
    return contagem_regressiva(n-1)

contagem_regressiva(n)