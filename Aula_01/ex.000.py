def somar(a, b):
    soma = 0
    soma = a + b
    return soma
def multiplicar(a, b):
    mult = a * b
    return mult

def subtrair(a, b):
    sub = a - b
    return sub

def dividir(a, b):
    div = a / b
    return div

op = 10
while op!=0:

    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))

    print("(1) Para somar ")
    print("(2) Para subtrair ")
    print("(3) Para multiplicar")
    print("(4) Para dividir")
    print("(0) Para sair ")
    op = int(input("ESCOLHA UMA OPERAÇÃO:"))

    match op:

        case 1:
            print(somar(n1, n2))

        case 2:
            print(subtrair(n1, n2))

        case 3:
            print(multiplicar(n1, n2))

        case 4:
            print(dividir(n1,n2))
