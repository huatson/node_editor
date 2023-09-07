"""
Editor Window
"""

# PyQt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout,
                             QGraphicsItem,
                             QPushButton,
                             QTextEdit)
from PyQt5.QtCore import QRectF, QLine, QFile, QIODevice, QPointF
from PyQt5.QtGui import QBrush, QColor, QPen, QFont

from node_editor.core_scene import Scene
from node_editor.editor_view import EditorView
from node_editor.core_node import Node
from node_editor.core_socket import Socket, ESocketType


DEFAULT_SIZE_W = 1024
DEFAULT_SIZE_H = 720


class EditorWindow(QWidget):
    def __init__(self, app: QApplication, parent=None) -> None:
        super(EditorWindow, self).__init__(parent)

        self.app = app

        # styles
        self._node_style_file = "D:\\dev\\WB\\node_editor\\node_editor\\styles\\node_style.qss"
        self.loadStyleSheet(self._node_style_file)

        # init UI
        self.initUI()

    def initUI(self):
        self.setGeometry(1500, 500, DEFAULT_SIZE_W, DEFAULT_SIZE_H)
        self.setWindowTitle("Node Editor")

        # layout
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)

        # scene
        self._core_scene = Scene()

        # view
        self._editor_view = EditorView(self._core_scene._editor_scene, self)
        self._layout.addWidget(self._editor_view)

        self.show()

    def _add_content_debug(self):
        """content samples"""
        green_brush = QBrush(QColor("#00A300"))
        outline_pen = QPen(QColor("#171717"))
        outline_pen.setWidth(2)
        rect_pos = QRectF(-100, -100, 100, 100)
        rect = self._core_scene._editor_scene.addRect(rect_pos, outline_pen, green_brush)
        rect.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        text = self._core_scene._editor_scene.addText("My awesome text", QFont("Ubuntu Mono"))
        text.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        button = QPushButton("push button")
        proxy_btn = self._core_scene._editor_scene.addWidget(button)
        proxy_btn.setPos(0, 30)

        input_text = QTextEdit()
        proxy_txtEdit = self._core_scene._editor_scene.addWidget(input_text)
        proxy_txtEdit.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        proxy_txtEdit.setPos(0, 60)

        line = self._core_scene._editor_scene.addLine(-200, -200, 100, 100, outline_pen)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def loadStyleSheet(self, filename: str):
        file = QFile(filename)
        file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text)
        style_sheet = file.readAll().data()
        self.app.setStyleSheet(str(style_sheet, encoding="utf-8"))
