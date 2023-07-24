from main_window import openWindow

if __name__ == "__main__":
    # Definining StyleSheet
    with open("application.css", "r", encoding="utf-8") as archive:
        cssStyleSheet = archive.read()

    openWindow(cssStyleSheet)
