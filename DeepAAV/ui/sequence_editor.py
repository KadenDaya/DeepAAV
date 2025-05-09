from PySide6.QtWidgets import QTextEdit

class SequenceEditor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlainText("# DNA/Protein sequence editor placeholder")
        # TODO: Add syntax highlighting, feature annotations, selection handling
