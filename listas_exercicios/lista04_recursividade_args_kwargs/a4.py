numeros = [1,2,3,4,5,6]

def filtra_lista(*numeros, **argumentos):
    start = int(argumentos.get('min'))
    stop = int(argumentos.get('max'))
    return numeros[start:stop]

print(filtra_lista(1,2,3,4,5,6, min=2, max=5))