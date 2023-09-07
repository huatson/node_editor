import unittest

from node_editor.editor_window import EditorWindow
from node_editor.core_scene import Scene
from node_editor.editor_view import EditorView
from node_editor.core_node import Node
from node_editor.core_socket import Socket, ESocketType
from PyQt5.QtWidgets import QApplication
import sys


class TetstCore(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = EditorWindow(self.app, None)
        self._core_scene = self.window._core_scene

    def test_nodes(self):
        # create inputs and outputs
        node_inputs = [1, 1, 1]
        node_outputs = [1, 1]

        # create sample nodes
        self.core_node_a = Node(self._core_scene, "my node A", node_inputs, node_outputs)
        self.core_node_a.setPos(-350, -200)
        self.core_node_b = Node(self._core_scene, "my node B", node_inputs, node_outputs)
        self.core_node_b.setPos(-75, 0)
        self.core_node_c = Node(self._core_scene, "my node C", node_inputs, node_outputs)
        self.core_node_c.setPos(200, -150)
        # add editor nodes to editor scene
        self._core_scene._editor_scene.addItem(self.core_node_a._editor_node)
        self._core_scene._editor_scene.addItem(self.core_node_b._editor_node)
        self._core_scene._editor_scene.addItem(self.core_node_c._editor_node)
        self.assertIsNotNone(self.core_node_a)
        self.assertIsNotNone(self.core_node_b)
        self.assertIsNotNone(self.core_node_c)


if __name__ == "__main__":
    unittest.main()
