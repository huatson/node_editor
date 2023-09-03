"""
Scene
"""

import math

# PyQt
from PyQt5.QtCore import QRectF, QLine
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QColor, QPainter, QPen


class NodeEditorScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(NodeEditorScene, self).__init__(parent)
        # colors
        self._color_background = QColor("#393939")
        self._color_light = QColor("#2F2F2F")
        self._color_dark = QColor("#292929")
        self._color_red = QColor("#750000")
        self._color_green = QColor("#007500")

        # grid
        self._grid_size = 20
        self._grid_squares = 5
        self._grid_guides_size = (self._grid_size*self._grid_squares)
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)
        self._pen_red = QPen(self._color_red)
        self._pen_red.setWidth(3)
        self._pen_green = QPen(self._color_green)
        self._pen_green.setWidth(3)

        # scene
        self._scene_width = 64000.0
        self._scene_height = 64000.0
        centered = QRectF(-self._scene_width//2,
                          -self._scene_height//2,
                          self._scene_width,
                          self._scene_height)
        self.setSceneRect(centered)
        self.setBackgroundBrush(self._color_background)

    def _draw_grid(self, painter: QPainter, rect: QRectF) -> None:
        area_left = int(math.floor(rect.left()))
        area_right = int(math.floor(rect.right()))
        area_top = int(math.floor(rect.top()))
        area_bottom = int(math.floor(rect.bottom()))

        edge_left = area_left - (area_left % self._grid_size)
        edge_top = area_top - (area_top % self._grid_size)

        background_lines = []
        guides_lines = []
        for x in range(edge_left, area_right, self._grid_size):
            if (x % self._grid_guides_size) != 0:
                background_lines.append(QLine(x, area_top, x, area_bottom))
            else:
                guides_lines.append(QLine(x, area_top, x, area_bottom))

        for y in range(edge_top, area_bottom, self._grid_size):
            if (y % self._grid_guides_size) != 0:
                background_lines.append(QLine(area_left, y, area_right, y))
            else:
                guides_lines.append(QLine(area_left, y, area_right, y))

        # red line
        red_line = QLine(0, -32000, 0, 32000)
        green_line = QLine(-32000, 0, 32000, 0)

        painter.setPen(self._pen_light)
        painter.drawLines(*background_lines)
        painter.setPen(self._pen_dark)
        painter.drawLines(*guides_lines)
        painter.setPen(self._pen_red)
        painter.drawLine(red_line)
        painter.setPen(self._pen_green)
        painter.drawLine(green_line)

    def drawBackground(self, painter: QPainter, rect: QRectF):
        super().drawBackground(painter, rect)
        self._draw_grid(painter, rect)
