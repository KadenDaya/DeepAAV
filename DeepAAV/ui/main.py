from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui     import QAction, QIcon
from ui.plasmid_visualizer import PlasmidVisualizer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AAV CAD — Plasmid Visualizer")
        self.resize(1000, 700)
        self._create_actions()
        self._create_menu_bar()
        self._create_central_widget()

    def _create_actions(self):
        self.exit_action = QAction(QIcon(), "E&xit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)

    def _create_menu_bar(self):
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(self.exit_action)

    def _create_central_widget(self):
        # define your three core AAV plasmids here
        plasmids = [
            {"name": "pHelper", "sequence": ""},
            {"name": "pAAV",    "sequence": ""},
            {"name": "pRC",     "sequence": ""},
        ]
        viz = PlasmidVisualizer(plasmids)
        self.setCentralWidget(viz)
