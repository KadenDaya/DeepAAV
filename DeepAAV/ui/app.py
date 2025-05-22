from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DeepAAV 0.0.1-alpha')

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow
    window.show()

    app.exec()