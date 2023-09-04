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

from node_editor.scene import NodeEditorScene
from node_editor.view import NodeEditorView


class NodeEditorWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super(NodeEditorWindow, self).__init__(parent)
        self._scene = NodeEditorScene()
        self._view = NodeEditorView(self._scene, self)

        self._layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1920, 1080)
        self.setWindowTitle("Node Editor")

        # layout
        self._layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self._layout)

        # scene

        # graphics view
        self._view.setScene(self._scene)
        self._layout.addWidget(self._view)

        self.show()
        self._add_content_debug()

    def _add_content_debug(self):
        green_brush = QBrush(QColor("#00A300"))
        outline_pen = QPen(QColor("#171717"))
        outline_pen.setWidth(2)
        rect_pos = QRectF(-100, -100, 100, 100)
        rect = self._scene.addRect(rect_pos, outline_pen, green_brush)
        rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        text = self._scene.addText("My awesome text", QFont("Ubuntu Mono"))
        text.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        button = QPushButton("push button")
        proxy_btn = self._scene.addWidget(button)
        proxy_btn.setPos(0, 30)

        input_text = QTextEdit()
        proxy_txtEdit = self._scene.addWidget(input_text)
        proxy_txtEdit.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        proxy_txtEdit.setPos(0, 60)

        line = self._scene.addLine(-200, -200, 100, 100, outline_pen)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
