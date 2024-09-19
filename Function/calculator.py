import math

def calculate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if number2 != 0:
            return number1 / number2
        else:
            return "Ділити на нуль , НЕ можна!"
    elif operator == "^":
        return number1 ** number2
    elif operator == "√":
        if number1 >= 0:
            return math.sqrt(number1)
        else:
            return "Це неможе бути від'ємне число!"
    elif operator == "%":
        if number2 != 0:
            return number1 % number2
        else:
            return "Ділення на нуль не допускається!"
    else:
        return "Некоректно введений оператор!"
