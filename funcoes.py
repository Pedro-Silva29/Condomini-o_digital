#Funcoes do primeiro exercicio da aula de python
def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

#Functions on the secound exercise of the python
def imprime_nome(nome):
    print(f"Nome: {nome}")

#funcoes do terceiro exercicio

#funcoes da aula 2 de python ex1
def vogais(t):
    cont = 0
    for i in t:
        if i in 'aeiouAEIOU':
            cont+=1
    print(cont)
nome = 'O rato roeu a roupa do rei de roma'
vogais(nome)

#funcoes da aula 2 de python ex2
def letras(t):
    cont = 0
    for i in t:
        if i != ' ':
            cont+=1
    print(cont)
nome = 'O rato roeu a roupa do rei de roma'
vogais(nome)



