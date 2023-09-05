"""
Content Widget Node
"""

# PyQt
from PyQt5.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QGraphicsItem,
                             QPushButton,
                             QTextEdit,
                             QLabel)
from PyQt5.QtCore import QRectF, QLine
from PyQt5.QtGui import QBrush, QColor


class ContentWidgetNode(QWidget):
    def __init__(self, parent=None) -> None:
        super(ContentWidgetNode, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)
        self._widget_label = QLabel("Widget Label")
        self._layout.addWidget(self._widget_label)
        self._layout.addWidget(QTextEdit("foo"))
