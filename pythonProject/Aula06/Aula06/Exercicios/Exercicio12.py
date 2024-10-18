def func():
    num1 = int(input("Digite o primeiro número"))
    num2 = int(input("Digite o segundo número"))

    quociente = num1 / num2
    resto = (num1 % num2)

    return quociente, resto

print(func())