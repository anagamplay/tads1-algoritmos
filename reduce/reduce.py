from functools import reduce

# sintaxe: reduce(function, iterable, [initializer])
# iterable é uma lista, tupla ou qualquer outro iterável.
# A função é aplicada cumulativamente aos itens do iterável, da esquerda para a direita, reduzindo o iterável a um único valor.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = reduce(lambda x, y: x + y, numbers)

from random import randint

random_numbers = [randint(1, 500) for _ in range(10)]
print(random_numbers)

max_value = reduce(lambda x, y: x if x > y else y, random_numbers)
print(max_value)
