"""
Core Connector
"""

from node_editor.core_socket import Socket
from node_editor.editor_connector import EditorConnector


class Connector(object):
    def __init__(self, scene: "Scene", start_socket: Socket, end_socket: Socket) -> None:
        self._scene = scene
        self._start_socket = start_socket
        self._end_socket = end_socket

        self._editor_connector = EditorConnector()
