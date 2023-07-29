from PyQt6 import QtWidgets
from main_window import MainWindow
import sys

if __name__ == "__main__":
    # Definining StyleSheet
    with open("application.css", "r", encoding="utf-8") as archive:
        cssStyleSheet = archive.read()

    # Opening window
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(cssStyleSheet)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
