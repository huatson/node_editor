"""
Window
"""

# PyQt
from PyQt5.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QGraphicsItem,
                             QPushButton,
                             QTextEdit)
from PyQt5.QtCore import QRectF, QLine
from PyQt5.QtGui import QBrush, QColor, QPen, QFont

from node_editor.core_scene import Scene
from node_editor.editor_view import NodeEditorView
from node_editor.core_node import Node


class NodeEditorWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super(NodeEditorWindow, self).__init__(parent)
        # scene
        self._scene = Scene()
        # self._editor_scene = self._scene._editor_scene

        # view
        self._view = NodeEditorView(self._scene._editor_scene, self)

        # layout
        self._layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1920, 1080)
        self.setWindowTitle("Node Editor")

        # layout
        self._layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self._layout)

        # sample node
        node = Node(self._scene, "my node")

        self._layout.addWidget(self._view)

        self.show()

        # self._add_content_debug()

    def _add_content_debug(self, editor_scene):
        green_brush = QBrush(QColor("#00A300"))
        outline_pen = QPen(QColor("#171717"))
        outline_pen.setWidth(2)
        rect_pos = QRectF(-100, -100, 100, 100)
        rect = editor_scene.addRect(rect_pos, outline_pen, green_brush)
        rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        text = editor_scene.addText("My awesome text", QFont("Ubuntu Mono"))
        text.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        button = QPushButton("push button")
        proxy_btn = editor_scene.addWidget(button)
        proxy_btn.setPos(0, 30)

        input_text = QTextEdit()
        proxy_txtEdit = editor_scene.addWidget(input_text)
        proxy_txtEdit.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        proxy_txtEdit.setPos(0, 60)

        line = editor_scene.addLine(-200, -200, 100, 100, outline_pen)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
