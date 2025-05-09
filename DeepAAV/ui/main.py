# ui/main.py

from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog
from PySide6.QtGui import QAction, QIcon

# If you have a SequenceEditor widget in ui/sequence_editor.py, import it:
try:
    from ui.sequence_editor import SequenceEditor
except ImportError:
    SequenceEditor = QWidget  # fallback to plain widget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeepAAV")
        self.resize(1200, 800)
        self._create_actions()
        self._create_menu_bar()
        self._create_central_widget()

    def _create_actions(self):
        self.open_action = QAction(QIcon(), "&Open...", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction(QIcon(), "&Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.save_file)

        self.exit_action = QAction(QIcon(), "E&xit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)

    def _create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

    def _create_central_widget(self):
        # Replace QWidget with your actual SequenceEditor if available
        self.editor = SequenceEditor()
        self.setCentralWidget(self.editor)

    def open_file(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, "Open Sequence File", "",
            "GenBank Files (*.gb);;FASTA Files (*.fasta)"
        )
        if fname:
            with open(fname, 'r') as f:
                data = f.read()
            self.editor.setPlainText(data)

    def save_file(self):
        fname, _ = QFileDialog.getSaveFileName(
            self, "Save Sequence File", "",
            "GenBank Files (*.gb);;FASTA Files (*.fasta)"
        )
        if fname:
            with open(fname, 'w') as f:
                f.write(self.editor.toPlainText())
