"""
Core Node
"""

from node_editor.editor_node import EditorNode
from node_editor.widget_node import ContentWidgetNode


class Node(object):
    def __init__(self, scene: "Scene", title: str = "node", inputs: list = [], outputs: list = []) -> None:
        self._scene = scene
        self._title = title

        self._content = ContentWidgetNode()
        self._editor_node = EditorNode(self, self._content)
        self._scene.add_node(self)

        self._inputs = inputs
        self._outputs = outputs
