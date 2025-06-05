from random import randint
from functools import reduce

random_numbers = [randint(1, 10) for _ in range(10)]

squared_num = list(map(lambda x: x**2, random_numbers))
result = reduce(lambda x, y: x + y, squared_num)/len(squared_num)

print(result)