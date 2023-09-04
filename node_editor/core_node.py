"""
Core Node
"""

from node_editor.editor_node import NodeEditorNode


class Node(object):
    def __init__(self, scene, title="node") -> None:
        self._scene = scene
        self._title = title
        self._editor_node = NodeEditorNode(self, self._title)
        self._scene.add_node(self)
        self._inputs = []
        self._outputs = []
