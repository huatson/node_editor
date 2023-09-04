"""
View
"""

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtGui import QPainter, QMouseEvent, QWheelEvent
from PyQt5.QtCore import Qt, QEvent


class NodeEditorView(QGraphicsView):
    def __init__(self, scene=None, parent=None):
        super(NodeEditorView, self).__init__(parent)
        self._scene = scene

        # zoom
        self._zoom_multiplier = 1.25
        self._zoom_value = 10
        self._zoom_step = 1
        self._zoom_range = [0, 10]

        # init
        self._init_view()
        self.setScene(self._scene)

    def _init_view(self) -> None:
        self.setRenderHints(QPainter.RenderHint.Antialiasing
                            | QPainter.RenderHint.TextAntialiasing
                            | QPainter.RenderHint.HighQualityAntialiasing)
        self.setViewportUpdateMode(self.ViewportUpdateMode.FullViewportUpdate)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def mouseLeftPressEvent(self, event: QMouseEvent):
        return super(NodeEditorView, self).mousePressEvent(event)

    def mouseRightPressEvent(self, event: QMouseEvent):
        release_event = QMouseEvent(QEvent.Type.MouseButtonRelease,
                                    event.localPos(),
                                    event.screenPos(),
                                    Qt.LeftButton,
                                    Qt.NoButton,
                                    event.modifiers())
        super(NodeEditorView, self).mouseReleaseEvent(release_event)
        self.setDragMode(self.DragMode.ScrollHandDrag)
        drag_event = QMouseEvent(event.type(),
                                 event.localPos(),
                                 event.screenPos(),
                                 Qt.LeftButton,
                                 event.buttons() | Qt.LeftButton,
                                 event.modifiers())
        super(NodeEditorView, self).mousePressEvent(drag_event)

    def mouseMiddlePressEvent(self, event: QMouseEvent):
        return super(NodeEditorView, self).mousePressEvent(event)

    def mouseLeftReleaseEvent(self, event: QMouseEvent):
        return super(NodeEditorView, self).mousePressEvent(event)

    def mouseRightReleaseEvent(self, event: QMouseEvent):
        fakeEvent = QMouseEvent(event.type(),
                                event.localPos(),
                                event.screenPos(),
                                Qt.LeftButton,
                                event.buttons() & ~Qt.LeftButton,
                                event.modifiers())
        super(NodeEditorView, self).mouseReleaseEvent(fakeEvent)
        self.setDragMode(self.DragMode.NoDrag)

    def mouseMiddleReleaseEvent(self, event: QMouseEvent):
        return super(NodeEditorView, self).mousePressEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouseLeftPressEvent(event)
        elif event.button() == Qt.MouseButton.RightButton:
            self.mouseRightPressEvent(event)
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.mouseMiddlePressEvent(event)
        else:
            super(NodeEditorView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouseLeftReleaseEvent(event)
        elif event.button() == Qt.MouseButton.RightButton:
            self.mouseRightReleaseEvent(event)
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.mouseMiddleReleaseEvent(event)
        else:
            super(NodeEditorView, self).mouseReleaseEvent(event)

    def wheelEvent(self, event: QWheelEvent):
        return super(NodeEditorView, self).wheelEvent(event)
