def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

while true:

    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))

    opcao = int(input("Selecione a opção: "
                      "1 - somar"
                      "2 - subtrair "
                      "3 - multiplicar "
                      "4 - subtrair "
                      "5 - sair "))

    if opcao == 5:
        break
    elif opccao == 1:
        print(somar(n1,n2))
    elif opcao == 2:
        print(subtrair(n1,n2))
    elif opcao == 3:
        print(multiplicar(n1,n2))
    elif opcao == 4:
        print(dividir(n1,n2))
    else:
        print("número inválido!!")
