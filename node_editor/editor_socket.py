"""
Editor Socket
"""

import typing
from PyQt5.QtWidgets import QWidget, QGraphicsItem, QGraphicsTextItem, QStyleOptionGraphicsItem, QGraphicsProxyWidget
from PyQt5.QtGui import QBrush, QColor, QPen, QFont, QPainter, QPainterPath
from PyQt5.QtCore import QRectF, Qt, QRect


class EditorSocket(QGraphicsItem):
    def __init__(self, parent=None) -> None:
        super(EditorSocket, self).__init__(parent)
        self._radius = 6
        self._outline_width = 1
        self._color_background = QColor("#FFFF7700")
        self._color_outline = QColor("#FF000000")

        self._pen = QPen(self._color_outline)
        self._pen.setWidthF(self._outline_width)
        self._brush = QBrush(self._color_background)

    def boundingRect(self):
        xy = -self._radius-self._outline_width
        wh = (2.0*self._radius+self._outline_width)
        rect = QRectF(xy, xy, wh, wh)
        # rect = rect.normalized()
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget=None):
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self._radius, -self._radius, self._radius*2, self._radius*2)
