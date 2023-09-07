"""
Core Node
"""

# PyQt5
from PyQt5.QtCore import QRectF, QPointF, QRect

# modules
from node_editor.editor_node import EditorNode
from node_editor.content_node import ContentNode
from node_editor.core_socket import Socket, ESocketType
from node_editor.core_scene import Scene


class Node(object):
    def __init__(self, core_scene: Scene,
                 title: str = "node",
                 inputs=[],
                 outputs=[]) -> None:
        self._core_scene = core_scene
        self._title = title

        self._content = ContentNode()
        self._editor_node = EditorNode(self, self._content)
        self._core_scene.add_node(self)

        self._inputs = inputs
        self._outputs = outputs

        self._socket_spacing = 22
        self._sockets = []

        # add sockets
        for (i, socket) in enumerate(self._inputs):
            pos = self.getSocketPos(i, ESocketType.INPUT_BOTTOM)
            socket = Socket(self, i, ESocketType.INPUT_BOTTOM, pos)
            self._sockets.append(socket)

        for (j, socket) in enumerate(self._outputs):
            pos = self.getSocketPos(i, ESocketType.OUTPUT_TOP)
            socket = Socket(self, j, ESocketType.OUTPUT_TOP, pos)
            self._sockets.append(socket)

    @property
    def pos(self) -> QPointF:
        return self._editor_node.pos()

    def getSocketPos(self, idx: int, type=ESocketType.INPUT_TOP) -> []:
        """Calculate and return socket position"""
        xpos = 0 if type in (ESocketType.INPUT_TOP, ESocketType.INPUT_BOTTOM) else self._editor_node._width
        idx_spaced = idx*self._socket_spacing
        if type in (ESocketType.INPUT_BOTTOM, ESocketType.OUTPUT_BOTTOM):
            # bottom position
            ypos = (self._editor_node._height
                    - self._editor_node._padding
                    - self._editor_node._edge_size) - idx_spaced
        else:
            # top position
            ypos = (self._editor_node._title_height
                    + self._editor_node._padding
                    + self._editor_node._edge_size) + idx_spaced
        return [xpos, ypos]

    def setPos(self, pos_x: int, pos_y: int) -> None:
        """set node's position"""
        self._editor_node.setPos(pos_x, pos_y)
