"""
Editor Connector
"""

from PyQt5.QtWidgets import QWidget, QGraphicsItem, QGraphicsTextItem, QStyleOptionGraphicsItem, QGraphicsProxyWidget, QGraphicsPathItem
from PyQt5.QtGui import QBrush, QColor, QPen, QFont, QPainter, QPainterPath
from PyQt5.QtCore import QRectF, Qt, QRect


class EditorConnector(QGraphicsPathItem):
    def __init__(self, core_connector, parent=None):
        super(EditorConnector, self).__init__(self, parent)
        # core connector
        self._core_connector = core_connector
