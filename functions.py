def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):

    if number2 == 0:
        return "Erro. Divisão impossível"
    else:
        return number1 / number2

def percentage(number1, number2):
    return (number1/number2)*100

def average(number1, number2):
    return (number1 + number2)/2
