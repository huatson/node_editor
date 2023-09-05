"""
Core Socket
"""
from enum import Enum
from node_editor.editor_socket import EditorSocket


class ESocketType(Enum):
    """
    Sockets types
    """
    INPUT = 0
    OUTPUT = 1


class Socket(object):
    def __init__(self, node, idx=0, type=ESocketType.INPUT, position=[0.0, 0.0]) -> None:
        self._node = node
        self._idx = idx
        self._type = type
        self._position = position
        self._editor_socket = EditorSocket(self._node._editor_node)
        self._editor_socket.setPos(self._position[0], self._position[1])
