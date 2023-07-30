from PyQt6 import QtWidgets, QtGui
from calculator_widget import operations


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # LAYOUTS
        # Main display of the window
        mainLayout = QtWidgets.QGridLayout()
        self.setLayout(mainLayout)
        # Grid for the buttons
        buttonsGrid = QtWidgets.QGridLayout()
        mainLayout.addLayout(buttonsGrid, 1, 0)


        # RESULTS DISPLAY
        self.display = QtWidgets.QTextEdit()
        mainLayout.addWidget(self.display, 0, 0)
        self.display.textChanged.connect(lambda: self.display.moveCursor(QtGui.QTextCursor.MoveOperation.End))

        # BUTTONS
        self.buttonPressed = False  # Turns True when some button is clicked
        button_inf = {
            "%": (0, 0, lambda: self.buttonToDisplay("%")),
            "x²": (0, 1, lambda: self.buttonToDisplay("²")),
            "C": (0, 2, self.display.clear),
            "←": (0, 3, self.backspace),
            "(": (1, 0, lambda: self.buttonToDisplay("(")),
            ")": (1, 1, lambda: self.buttonToDisplay(")")),
            "√": (1, 2, lambda: self.buttonToDisplay("√(")),
            "÷": (1, 3, lambda: self.buttonToDisplay("÷")),
            "7": (2, 0, lambda: self.buttonToDisplay("7")),
            "8": (2, 1, lambda: self.buttonToDisplay("8")),
            "9": (2, 2, lambda: self.buttonToDisplay("9")),
            "x": (2, 3, lambda: self.buttonToDisplay("x")),
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
            "=": (5, 3, lambda: operations.calculateDisplay(self.display))
        }
        for key, value in button_inf.items():
            _row, _column, _function = value
            button = QtWidgets.QPushButton(key)
            button.clicked.connect(_function)
            buttonsGrid.addWidget(button, _row, _column)
            buttonsGrid.setRowStretch(_row, 1)
            buttonsGrid.setColumnStretch(_column, 1)

    # METHODS
    def buttonToDisplay(self, arg: str):
        self.display.insertPlainText(arg)

    def backspace(self):
        currentText = self.display.toPlainText()
        self.display.setPlainText(currentText[0: len(currentText) - 1])

    def setButtonPressed(self, status: bool):
        self.buttonPressed = status
