from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt

class CurrencyConverter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QComboBox{
            font-size: 30px;
            color: white;
        }
        QLineEdit{
            font-size: 30px;
            color: white
        }
        QLabel{
            font-size: 30px
            color: white
        }
        """)

        # Layout
        mainLayout = QtWidgets.QGridLayout()
        self.setLayout(mainLayout)

        # Display
        self.display = QtWidgets.QLineEdit()
        mainLayout.addWidget(self.display, 0, 0, 1, 3)

        # Options
        self.option1 = QtWidgets.QComboBox()
        self.option1.addItems(["Real (R$)", "Dólar ($)"])
        self.option2 = QtWidgets.QComboBox()
        self.option2.addItems(["Real (R$)", "Dólar ($)"])

        mainLayout.addWidget(self.option1, 1, 0)
        mainLayout.addWidget(self.option2, 1, 2)

        # Images
        self.arrow = QtWidgets.QLabel()
        self.arrow.setStyleSheet("""
        border-image: url('images/currency_converter_images/white_arrow.png') 0 0 0 0 stretch stretch;
        """)
        mainLayout.addWidget(self.arrow, 1, 1)

        # Button
        self.button = QtWidgets.QPushButton("Convert")
        mainLayout.addWidget(self.button, 2, 1)
