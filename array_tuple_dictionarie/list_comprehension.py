my_list = [1, 2, 3, 4, 5, 6]
squared = [x**2 for x in my_list if x % 2 == 0] 
even = [x for x in my_list if x % 2 == 0] 

print(squared, even)
