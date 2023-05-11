def calculo(num):
    if num != 0:
        if num == 2 % 0:
            return "P"
        else:
            return "N"
    else:
        return "Z"

num = input("Digite o numero: ")

print(calculo(num))
