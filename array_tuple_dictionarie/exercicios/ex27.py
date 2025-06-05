print('Essa é sua plilha')
print('1 - adicionar item à plilha')
print('2 - remover item da pilha')

num = input()
pilha = []

if num == 1:
    value = input('Insira o valor que deseja adicionar na pilha: ')
    pilha.append(value)
else:
    pilha.pop()