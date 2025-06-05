from random import randint
from functools import reduce

random_numbers = [randint(1, 10) for _ in range(10)]

squared_num = list(map(lambda x: x**3, random_numbers))
primos = filter(lambda x: x % 2 != 0)
result = reduce(lambda x, y: x if x > y else y, primos)

print(result)