print('\n================= Args e Kwargs =================\n')

# def minha_funcao(*args, **kwargs):
#     print("Argumentos posicionais:", args)
#     print("Argumentos nomeados:", kwargs)

#  os parametros obrigatórios vem primeiro, depois os opcionais

def minha_funcao(a, b, *args, **kwargs):
    print("Argumentos obrigatórios:", a, b)
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)

# '*args' é a abreviação de "arguments" e **kwargs é a abreviação de "keyword arguments"
#  Ambos permitem que você passe uma quantidade variável de argumentos para uma função.


minha_funcao(1, 2, [3, 4], 5, 6, nome="João", idade=30) 

# args retorna uma tupla com os argumentos posicionais extras
# kwargs retorna um dicionário com os argumentos nomeados extras
print('\n================= Subslistas =================\n')

qtd_sub_lista = 0

def sub_listas_com_recursao(lista, *args):
    global qtd_sub_lista

    print("Lista original:", lista)
    print("- Sub-listas:", args)

    for sub_lista in args:
        if isinstance(sub_lista, list):
            sub_listas_com_recursao(lista, *sub_lista)
        qtd_sub_lista += 1


sub_listas_com_recursao([1, 2, 3], [4, 5], [6, 7], [8, 9, [10, 11]])
print("\nQuantidade de sub-listas:", qtd_sub_lista)

print('\n================= X =================\n')

# Exercicios: implemente uma calculadora que leia dois tipos (soma, multiplicação), lista de números, parametro nomeado exibir_detalhes=True
def calculadora(tipo, numeros, **kwargs):
    resultado = 0
    detalhes = kwargs.get('exibir_detalhes', False)

    if tipo == 'soma':
        resultado = sum(numeros)
    elif tipo == 'multiplicacao':
        resultado = 1
        for num in numeros:
            resultado *= num
    else:
        raise ValueError("Tipo inválido. Use 'soma' ou 'multiplicacao'.")

    if detalhes:
        print(f"Tipo de operação: {tipo}")
        print(f"Números: {numeros}")
    
    return resultado