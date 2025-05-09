from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPainter

class PlasmidVisualizer(QWidget):
    def __init__(self, plasmids, parent=None):
        super().__init__(parent)
        self.plasmids = plasmids  # list of dicts: {'name': str, 'sequence': str}
        self.tabs = QTabWidget()
        # enable gesture‐style swiping on touchscreens
        self.tabs.setTabPosition(QTabWidget.North)
        for p in self.plasmids:
            self.tabs.addTab(self._create_plasmid_view(p), p['name'])
        self.tabs.addTab(self._create_all_view(), "All Plasmids")

        layout = QVBoxLayout(self)
        layout.addWidget(self.tabs)

    def _create_plasmid_view(self, plasmid):
        view = QGraphicsView()
        scene = QGraphicsScene()
        radius = 150
        # draw backbone circle
        scene.addEllipse(-radius, -radius, radius*2, radius*2,
                         brush=QBrush(QColor(220, 220, 255)))
        # label at center
        text_item = scene.addText(plasmid['name'])
        text_item.setPos(-text_item.boundingRect().width()/2, -10)
        view.setScene(scene)
        view.setRenderHint(QPainter.Antialiasing)
        view.setAlignment(Qt.AlignCenter)
        return view

    def _create_all_view(self):
        container = QWidget()
        v = QVBoxLayout(container)
        for p in self.plasmids:
            v.addWidget(QLabel(p['name']))
            v.addWidget(self._create_plasmid_view(p))
        container.setLayout(v)
        return container
