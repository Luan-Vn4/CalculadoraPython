from PyQt6.QtWidgets import QTextEdit
from math import *

def calculateDisplay(display: QTextEdit):
    currentText = __organizeExpression(display.toPlainText())
    try:
        display.setPlainText(str(eval(currentText)))
    except (NameError, SyntaxError):
        pass


def calculateStr(expression: str):
    organizedExpression = __organizeExpression(expression)
    try:
        return eval(organizedExpression)
    except (NameError, SyntaxError):
        return expression


def __organizeExpression(expression: str):
    # PERCENTAGE OPERATION
    index, number, operation = 0, "", None
    # It verifies each % symbol in the expression, identifies the previous numbers and operation and replace in the str
    while index != -1:
        number = ""
        operation = None
        index = expression.find("%", index+1)
        for i in range(index - 1, 0, -1):
            if expression[i].isnumeric() or expression[i] in "x÷+-":
                if expression[i].isnumeric():
                    number = expression[i] + number
                elif expression[i] == "+":
                    operation = "add"
                    break
                elif expression[i] == "-":
                    operation = "sub"
                    break
                elif expression[i] == "x":
                    operation = "mult"
                    break
                elif expression[i] == "÷":
                    operation = "div"
                    break
                else:
                    break

        match operation:
            case "add":
                expression = expression.replace(f"+{number}%", f"*{(1+(float(number)/100))}")
            case "sub":
                expression = expression.replace(f"-{number}%", f"*{(1-(float(number) / 100))}")
            case "mult":
                expression = expression.replace(f"x{number}%", f"*{(float(number) / 100)}")
            case "div":
                expression = expression.replace(f"÷{number}%", f"*{(100 / float(number))}")
            case _:
                break

    # Other Operations
    expression = expression.replace("√(", "sqrt(")
    expression = expression.replace("²", "**2")
    expression = expression.replace("÷", "/")
    expression = expression.replace("x", "*")

    return expression
