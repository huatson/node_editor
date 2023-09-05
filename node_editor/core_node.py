"""
Core Node
"""

from node_editor.editor_node import EditorNode
from node_editor.content_node import ContentNode
from node_editor.core_socket import Socket, ESocketType


class Node(object):
    def __init__(self, scene: "Scene",
                 title: str = "node",
                 inputs=[],
                 outputs=[]) -> None:
        self._scene = scene
        self._title = title

        self._content = ContentNode()
        self._editor_node = EditorNode(self, self._content)
        self._scene.add_node(self)

        self._inputs = inputs
        self._outputs = outputs

        self._socket_spacing = 22
        self._sockets = []

        for (i, socket) in enumerate(self._inputs):
            pos = self.getSocketPos(i, ESocketType.INPUT)
            socket = Socket(self, i, ESocketType.INPUT, pos)
            self._sockets.append(socket)

        for (j, socket) in enumerate(self._outputs):
            pos = self.getSocketPos(i, ESocketType.OUTPUT)
            socket = Socket(self, j, ESocketType.OUTPUT, pos)
            self._sockets.append(socket)

    def getSocketPos(self, idx: int, type=ESocketType.INPUT) -> []:
        xpos = 0 if type == ESocketType.INPUT else self._editor_node._width
        ypos = (
            self._editor_node._title_height +
            self._editor_node._padding +
            self._editor_node._edge_size) + (idx*self._socket_spacing)
        return [xpos, ypos]
