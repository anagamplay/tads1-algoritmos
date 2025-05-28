def only_unique(my_list):
    for x in my_list[:]:
        if my_list.count(x) > 1:
            my_list.remove(x)
    return my_list

print(only_unique([3, 2, 3, 2, 2, 3, 5]))