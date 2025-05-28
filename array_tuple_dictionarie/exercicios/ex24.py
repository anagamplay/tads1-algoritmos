num_list = [x for x in range(20)]

even_nums = [x for x in num_list if x % 2 == 0]
odd_nums = [x for x in num_list if x % 2 != 0]

print(f"Números pares: {even_nums}")
print(f"Números impares: {odd_nums}")