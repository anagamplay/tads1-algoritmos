num_list = []
repetition = 10

while len(num_list) < repetition:
    try:
        num = int(input('Insira um número: '))
        num_list.append(num)
    except ValueError:
        print('Entrada inválida. Tente novamente.')
        
num_list = [x for x in num_list if x % 2 != 0]
print(num_list)