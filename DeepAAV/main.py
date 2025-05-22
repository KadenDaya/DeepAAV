import sys
from PySide6.QtWidgets import QApplication
from ui.app import MainWindow

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
