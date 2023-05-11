def vogais(t):
    cont = 0
    for i in t:
        if i in 'aeiouAEIOU':
            cont+=1
    print(cont)
nome = 'O rato roeu a roupa do rei de roma'
vogais(nome)