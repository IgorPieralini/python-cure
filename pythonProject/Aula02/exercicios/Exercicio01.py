import colorama

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if(num1 < num2):
    print(colorama.Fore.GREEN + "o Primeiro número é o Menor: ", num1)
if(num1 > num2):
    print(colorama.Fore.GREEN + "o Segundo número é o Menor: ", num2)
if(num1 == num2):
    print(colorama.Fore.RED + "Os números são iguais")