"""
Scene
"""

# PyQt
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QColor


class NodeEditorScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(NodeEditorScene, self).__init__(parent)
        self._dark_color = QColor("#393939")
        self._scene_width = 64000
        self._scene_height = 64000
        self.setBackgroundBrush(self._dark_color)
