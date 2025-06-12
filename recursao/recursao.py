'''
Recursão é uma técnica de programação onde uma função chama a si mesma para resolver um problema.

Principais características:
- Base Case: Condição que encerra a recursão.
- Recursive Case: Parte da função que chama a si mesma.
- Pode ser mais intuitiva para problemas que possuem uma estrutura recursiva, como árvores e grafos.
- Bubble Sort: Algoritmo de ordenação que utiliza recursão.
'''

# Exemplo de recursão simples: calcular fatorial de um número


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


print(fatorial(5))  # Saída: 120

# Sequência de Fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))

# soma dos elementos de uma lista usando recursão

def soma(lista):
    return
