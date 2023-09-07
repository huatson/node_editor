"""
Editor node
"""

from PyQt5.QtWidgets import QWidget, QGraphicsItem, QGraphicsTextItem, QStyleOptionGraphicsItem, QGraphicsProxyWidget
from PyQt5.QtGui import QBrush, QColor, QPen, QFont, QPainter, QPainterPath
from PyQt5.QtCore import QRectF, Qt, QRect
from node_editor.content_node import ContentNode
import math

# from node_editor.core_node import Node as NodeClass


class EditorNode(QGraphicsItem):
    def __init__(self, core_node, content: ContentNode, parent=None) -> None:
        super(EditorNode, self).__init__(parent)
        self._core_node = core_node
        self._content = content
        # colors
        self._color_background = QColor("#393939")
        self._color_light = QColor("#2F2F2F")
        self._color_dark = QColor("#292929")
        self._color_red = QColor("#750000")
        self._color_green = QColor("#007500")
        self._title_color = QColor("#7F0000")
        self._selected = QColor("#FFFFA637")
        self._title_brush_color = QColor("#FF313131")
        self._title_brush_background_color = QColor("#E3212121")

        # title
        self._title_color = QColor(QColor.fromRgbF(1.0, 1.0, 1.0))
        self._title_font = QFont("Ubuntu", pointSize=10)
        self._title_item = QGraphicsTextItem(self)
        self._title_brush = QBrush(self._title_brush_color)
        self._title_brush_background = QBrush(self._title_brush_background_color)

        # size
        self._width = 180.0
        self._height = 256.0
        self._edge_size = 12.0
        self._title_height = 24.0
        self._padding = 5.0

        # pens
        self._pen_outline = QPen(self._color_dark)
        self._pen_outline.setWidth(3)

        self._pen_selected = QPen(self._selected)
        self._pen_selected.setWidth(3)

        # init title
        self.initTitle()
        self.title = self._core_node._title

        # content
        self.initContent()

        # init UI
        self.initUI()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value
        if self._title_item:
            self._title_item.setPlainText(self._title)

    def initUI(self):
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setAcceptHoverEvents(True)

    def initTitle(self):
        self._title_item.setDefaultTextColor(self._title_color)
        self._title_item.setFont(self._title_font)
        self._title_item.setTextWidth(self._width-2.0*self._padding)
        self._title_item.setPos(self._padding, 0.0)

    def initContent(self):
        self._node_content = QGraphicsProxyWidget(self)

        ax = int(self._edge_size)
        ay = math.floor(self._title_height+self._edge_size)
        aw = math.floor(self._width-2.0*self._edge_size)
        ah = math.floor(self._height-2.0*self._edge_size-self._title_height)
        content_rect = QRect(ax, ay, aw, ah)

        if not self._content:
            return
        self._content.setGeometry(content_rect)
        self._node_content.setWidget(self._content)

    def boundingRect(self):
        rect = QRectF(0, 0, self._width, self._height)
        return rect.normalized()

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget=None):
        # tittle
        title_path = QPainterPath()
        title_path.setFillRule(Qt.FillRule.WindingFill)
        title_rect = QRectF(0.0, 0.0, self._width, self._title_height)
        title_path.addRoundedRect(title_rect, self._edge_size, self._edge_size)
        title_path.addRect(0.0, (self._title_height-self._edge_size), self._edge_size, self._edge_size)
        title_path.addRect((self._width-self._edge_size),
                           (self._title_height-self._edge_size),
                           self._edge_size,
                           self._edge_size)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._title_brush)
        painter.drawPath(title_path.simplified())

        # content
        content = QPainterPath()
        content.setFillRule(Qt.FillRule.WindingFill)
        content_rect = QRectF(0.0, self._title_height, self._width, self._height-self._title_height)
        content.addRoundedRect(content_rect, self._edge_size, self._edge_size)
        content.addRect(0.0, self._title_height, self._edge_size, self._edge_size)
        content.addRect(self._width-self._edge_size, self._title_height, self._edge_size, self._edge_size)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._title_brush_background)
        painter.drawPath(content.simplified())

        # outline
        outline_path = QPainterPath()
        shape_rect = QRectF(0.0, 0.0, self._width, self._height)
        outline_path.addRoundedRect(shape_rect, self._edge_size, self._edge_size)
        target_pen = self._pen_outline if not self.isSelected() else self._pen_selected
        painter.setPen(target_pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawPath(outline_path.simplified())
