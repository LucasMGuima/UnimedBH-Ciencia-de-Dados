casos = {'nenhuma': 'portugues', 
        'esquerda': 'ingles', 
        'direita': 'frances', 
        'ambas': 'caiu'}

while True:
    try:
        caso = input().lower()
        print(casos[caso])
    except EOFError:
        break