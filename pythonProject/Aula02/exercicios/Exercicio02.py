import colorama

number = int(input("Digite um número: "))

if(number % 2 == 0 ):
    print(colorama.Fore.LIGHTWHITE_EX, "O número:" + colorama.Fore.BLUE, number, colorama.Fore.LIGHTWHITE_EX + colorama.Back.GREEN +  "É par"+ colorama.Back.RESET)
else:
    print(colorama.Fore.LIGHTWHITE_EX, "O número:" + colorama.Fore.BLUE, number, colorama.Fore.LIGHTWHITE_EX + colorama.Back.RED + "É impar" + colorama.Back.RESET)