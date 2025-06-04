# anonymous functions

double = lambda x: x * 2
print('Example 1 - double 5:', double(5))

sum_numbers = lambda x, y: x + y
print('Example 2 - sum 5 and 10:', sum_numbers(5, 10))

hypotenuse = lambda catOp, catAd: (catOp**2 + catAd**2)**0.5
print('Example 3 - hypotenuse of a triangle with catOp 3 and catAd 4:', hypotenuse(3, 4))

import math
hypotenuse2 = lambda a, b: math.sqrt(a**2 + b**2)
print('Example 4 - hypotenuse of a triangle with catOp 5 and catAd 12:', hypotenuse2(5, 12))

# filter, map

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print('Example 5 - even numbers from 1 to 10:', even_numbers)

import random
random_numbers = [random.randint(20, 100) for _ in range(100)]
greater_then_60 = list(filter(lambda x: x > 60, random_numbers))
print('Example 6 - random numbers greater than 60:', greater_then_60)

greater_then_average = list(filter(lambda x: x > sum(random_numbers[:])/100, random_numbers))
print('Example 7 - random numbers greater than average:', greater_then_average)

# map for transformation
squared_numbers = list(map(lambda x: x**2, numbers))
print('Example 8 - squared numbers from 1 to 10:', squared_numbers)

# sorted(list, key=lambda x: x[1])
students = [('John', 85), ('Jane', 92), ('Dave', 78), ('Alice', 95)]
print('Example 9 - students sorted by score:', sorted(students, key=lambda x: x[1]))