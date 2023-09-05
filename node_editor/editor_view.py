"""
Editor View
"""

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtGui import QPainter, QMouseEvent, QWheelEvent
from PyQt5.QtCore import Qt, QEvent, QPoint, pyqtSignal


class EditorView(QGraphicsView):
    #: pyqtSignal emitted when cursor position on the `Scene` has changed
    scenePosChanged = pyqtSignal(int, int)

    def __init__(self, scene=None, parent=None):
        super(EditorView, self).__init__(parent)
        self._scene = scene

        # init
        self.initUI()
        self.setScene(self._scene)

        # zoom
        self._zoom_in_multiplier = 1.25
        self._zoom_out_multiplier = (1.0/self._zoom_in_multiplier)
        self._zoom_value = 0
        self._zoom_step = 1
        self._zoom_range = [-5, 10]
        self._zoom_clamp = True
        self.last_scene_mouse_position = QPoint(0, 0)

    def initUI(self) -> None:
        self.setRenderHints(QPainter.RenderHint.Antialiasing
                            | QPainter.RenderHint.TextAntialiasing
                            | QPainter.RenderHint.HighQualityAntialiasing
                            | QPainter.RenderHint.SmoothPixmapTransform)
        self.setViewportUpdateMode(self.ViewportUpdateMode.FullViewportUpdate)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(self.DragMode.RubberBandDrag)
        self.setAcceptDrops(True)

    # PRESS EVENTS

    def mouseLeftPressEvent(self, event: QMouseEvent):
        super(EditorView, self).mousePressEvent(event)

    def mouseRightPressEvent(self, event: QMouseEvent):
        release_event = QMouseEvent(QEvent.Type.MouseButtonRelease,
                                    event.localPos(),
                                    event.screenPos(),
                                    Qt.MouseButton.LeftButton,
                                    Qt.MouseButton.NoButton,
                                    event.modifiers())
        super(EditorView, self).mouseReleaseEvent(release_event)
        self.setDragMode(self.DragMode.ScrollHandDrag)
        drag_event = QMouseEvent(event.type(),
                                 event.localPos(),
                                 event.screenPos(),
                                 Qt.MouseButton.LeftButton,
                                 event.buttons() | Qt.MouseButton.LeftButton,
                                 event.modifiers())
        super(EditorView, self).mousePressEvent(drag_event)

    def mouseMiddlePressEvent(self, event: QMouseEvent):
        super(EditorView, self).mousePressEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouseLeftPressEvent(event)
        elif event.button() == Qt.MouseButton.RightButton:
            self.mouseRightPressEvent(event)
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.mouseMiddlePressEvent(event)
        else:
            super(EditorView, self).mousePressEvent(event)

    # RELEASE EVENTS

    def mouseLeftReleaseEvent(self, event: QMouseEvent):
        super(EditorView, self).mouseReleaseEvent(event)

    def mouseRightReleaseEvent(self, event: QMouseEvent):
        release_event = QMouseEvent(event.type(),
                                    event.localPos(),
                                    event.screenPos(),
                                    Qt.MouseButton.LeftButton,
                                    event.buttons() & ~Qt.MouseButton.LeftButton,
                                    event.modifiers())
        super(EditorView, self).mouseReleaseEvent(release_event)
        self.setDragMode(self.DragMode.NoDrag)

    def mouseMiddleReleaseEvent(self, event: QMouseEvent):
        super(EditorView, self).mouseReleaseEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouseLeftReleaseEvent(event)
        elif event.button() == Qt.MouseButton.RightButton:
            self.mouseRightReleaseEvent(event)
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.mouseMiddleReleaseEvent(event)
        else:
            super(EditorView, self).mouseReleaseEvent(event)

    # WHEEL

    def wheelEvent(self, event: QWheelEvent):
        self._zoom_out_multiplier = (1.0/self._zoom_in_multiplier)
        angre_delta_y = event.angleDelta().y()
        if angre_delta_y > 0:
            zoom_scale = self._zoom_in_multiplier
            self._zoom_value += self._zoom_step
        else:
            zoom_scale = self._zoom_out_multiplier
            self._zoom_value -= self._zoom_step
        is_clamped = False
        if self._zoom_value < self._zoom_range[0]:
            self._zoom_value = self._zoom_range[0]
            is_clamped = True
        if self._zoom_value > self._zoom_range[1]:
            self._zoom_value = self._zoom_range[1]
            is_clamped = True
        if not is_clamped or not self._zoom_clamp:
            self.scale(zoom_scale, zoom_scale)

    def mouseMoveEvent(self, event: QMouseEvent):
        """Overriden Qt's ``mouseMoveEvent`` handling Scene/View logic"""
        scenepos = self.mapToScene(event.pos())
        self.last_scene_mouse_position = scenepos
        self.scenePosChanged.emit(int(scenepos.x()), int(scenepos.y()))
        super(EditorView, self).mouseMoveEvent(event)
