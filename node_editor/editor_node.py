"""
Editor node
"""

from PyQt5.QtWidgets import QGraphicsItem


class NodeEditorNode(QGraphicsItem):
    def __init__(self, core_node, title="node") -> None:
        self._core_node = core_node
        self._title = title
        self.init_ui()

    def init_ui(self):
        pass
