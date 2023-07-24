from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
import sys, operations

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.resize(400, 600)
        self.setWindowIcon(QtGui.QIcon("calculator.png"))


        # Layouts
        mainLayout = QtWidgets.QGridLayout()
        self.setLayout(mainLayout)

        buttonsGrid = QtWidgets.QGridLayout()
        mainLayout.addLayout(buttonsGrid, 1, 0)


        # Results display
        self.display = QtWidgets.QTextEdit()
        mainLayout.addWidget(self.display, 0, 0)


        # Buttons
        button_inf = {
            "%": (0, 0, lambda: self.buttonToDisplay("%")),
            "x²": (0, 1, lambda: self.buttonToDisplay("²")),
            "C": (0, 2, self.display.clear),
            "←": (0, 3, self.backspace),
            "(": (1, 0, lambda: self.buttonToDisplay("(")),
            ")": (1, 1, lambda: self.buttonToDisplay(")")),
            "√": (1, 2, lambda: self.buttonToDisplay("√")),
            "÷": (1, 3, lambda: self.buttonToDisplay("÷")),
            "7": (2, 0, lambda: self.buttonToDisplay("7")),
            "8": (2, 1, lambda: self.buttonToDisplay("8")),
            "9": (2, 2, lambda: self.buttonToDisplay("9")),
            "X": (2, 3, lambda: self.buttonToDisplay("X")),
            "4": (3, 0, lambda: self.buttonToDisplay("4")),
            "5": (3, 1, lambda: self.buttonToDisplay("5")),
            "6": (3, 2, lambda: self.buttonToDisplay("6")),
            "-": (3, 3, lambda: self.buttonToDisplay("-")),
            "1": (4, 0, lambda: self.buttonToDisplay("1")),
            "2": (4, 1, lambda: self.buttonToDisplay("2")),
            "3": (4, 2, lambda: self.buttonToDisplay("3")),
            "+": (4, 3, lambda: self.buttonToDisplay("+")),
            "00": (5, 0, lambda: self.buttonToDisplay("00")),
            "0": (5, 1, lambda: self.buttonToDisplay("0")),
            ".": (5, 2, lambda: self.buttonToDisplay(".")),
            "=": (5, 3, self.calculate),
        }
        for key, value in button_inf.items():
            _row, _column, _function = value
            button = QtWidgets.QPushButton(key)
            button.clicked.connect(_function)
            buttonsGrid.addWidget(button, _row, _column)
            buttonsGrid.setRowStretch(_row, 1)
            buttonsGrid.setColumnStretch(_column, 1)


    def buttonToDisplay(self, arg: str):
        self.display.insertPlainText(arg)

    def backspace(self):
        currentText = self.display.toPlainText()
        self.display.setPlainText(currentText[0: len(currentText) - 1])
        self.display.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def calculate(self):
        import math
        currentText = self.display.toPlainText()
        currentText.replace("\n", "").replace("√", "sqrt").replace("²", "**2").replace("X", "*")
        try:
            result = eval(currentText)
            print(result)
            self.display.setPlainText(str(result))
        except (NameError, SyntaxError):
            pass

def openWindow(archive: str):
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(archive)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
