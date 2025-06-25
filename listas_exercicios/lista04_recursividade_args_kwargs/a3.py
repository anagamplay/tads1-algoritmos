def saudar(**kwargs):
    nome = kwargs.get('nome', 'você')
    idade = kwargs.get('idade', 'X')
    cidade = kwargs.get('cidade', 'Três Lagos')
    print(f"Olá, {nome} de {idade} anos, morador(a) de {cidade}!")
    
saudar()