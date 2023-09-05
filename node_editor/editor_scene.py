"""
Editor Scene
"""

# PyQt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QRectF, QLine
import math


class EditorScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super(EditorScene, self).__init__(parent)
        # core scene
        self._core_scene = scene
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

        # size defaults
        self._scene_w = 64000.0
        self._scene_h = 64000.0

        self.setBackgroundBrush(self._color_background)

    def setEditorScene(self, width: float, height: float):
        self._scene_h = height
        self._scene_w = width
        centered = QRectF(-width//2.0, -height//2.0, width, height)
        self.setSceneRect(centered)

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
        middle_scene_x = math.floor(self._scene_w//2)
        middle_scene_y = math.floor(self._scene_h//2)
        red_line = QLine(0, -middle_scene_x, 0, middle_scene_x)
        green_line = QLine(-middle_scene_y, 0, middle_scene_y, 0)

        painter.setPen(self._pen_light)
        painter.drawLines(*background_lines)
        painter.setPen(self._pen_dark)
        painter.drawLines(*guides_lines)
        painter.setPen(self._pen_red)
        painter.drawLine(red_line)
        painter.setPen(self._pen_green)
        painter.drawLine(green_line)

    def drawBackground(self, painter: QPainter, rect: QRectF):
        super(EditorScene, self).drawBackground(painter, rect)
        self._draw_grid(painter, rect)
