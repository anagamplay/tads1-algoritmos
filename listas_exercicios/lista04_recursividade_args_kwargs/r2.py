texto = input('Digite um texto: ')

def string_invertida(texto: str):
    if texto == "":
        return
    print(texto[-1], end='')  
    return string_invertida(texto[:-1]) 

texto = input('Digite um texto: ')
string_invertida(texto)
