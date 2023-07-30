from PyQt6 import QtWidgets, QtGui
from calculator_widget import calculator
from currencyWidget import currency_converter


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.resize(400, 600)
        self.setWindowIcon(QtGui.QIcon("images/main_window_images/calculator.png"))

        # Window Layout
        self.mainLayout = QtWidgets.QGridLayout()
        self.setLayout(self.mainLayout)

        # TabWidgets // Pages organizer
        self.pages = QtWidgets.QTabWidget()
        self.mainLayout.addWidget(self.pages)

        # Layouts/Pages
        calculatorPage = calculator.Calculator()
        self.pages.addTab(calculatorPage, "Calculator")
        currencyPage = currency_converter.CurrencyConverter()
        self.pages.addTab(currencyPage, "Currency")

