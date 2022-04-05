import os
from functions import addition, average, percentage, subtraction, multiplication, division

while True:
    print(" _____________________")
    print("|                     |")
    print("|-----CALCULADORA-----|")
    print("|                     |")
    print("|-----1 Adição--------|")  
    print("|-----2 Subtração-----|")
    print("|-----3 Multiplicação-|")
    print("|-----4 Divisão-------|")
    print("|-----5 Porcentagem---|")
    print("|-----6 Média---------|")
    print("|-----7 Sair----------|")
    print("|_____________________|\n")
    option = input("Opção: ")

    if option != '7' and option < '8' and option > '0':
        number1 = int(input("Informe um número: "))
        number2 = int(input("Informe um número: "))


        if option == '1':
            res = addition(number1, number2)
        elif option == '2':
            res = subtraction(number1, number2)
        elif option == '3':
            res = multiplication(number1, number2)
        elif option == '4':
            res = division(number1, number2)
        elif option == '5':
            res = percentage(number1, number2)
        elif option == '6':
            res = average(number1, number2)

        print("\nResultado: ", res)
        os.system("pause")


    else:
        print("Opção Inválida!")
        os.system("pause") 

    if not option!='7':
        print("Saindo...")
        break