"""
Window
"""


# PyQt
from PyQt5.QtWidgets import (QWidget,
                             QGraphicsView,
                             QVBoxLayout)

from node_editor.scene import NodeEditorScene


class NodeEditorWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super(NodeEditorWindow, self).__init__(parent)
        self._graphics_view = QGraphicsView(self)
        self._graphics_scene = NodeEditorScene()
        self._layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("Node Editor")

        # layout
        self._layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self._layout)

        # scene

        # graphics view
        self._graphics_view.setScene(self._graphics_scene)
        self._layout.addWidget(self._graphics_view)

        self.show()
