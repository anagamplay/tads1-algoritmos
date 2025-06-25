digitos = int(input('Insira um número inteiro positivo: '))

def soma_digitos(n):
    if n < 10:
        return n
    ultimo = n % 10
    resto = n // 10
    return ultimo + soma_digitos(resto)

print("Soma dos dígitos:", soma_digitos(digitos))