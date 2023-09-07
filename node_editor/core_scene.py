"""
Core Scene
"""

from node_editor.editor_scene import EditorScene


class Scene(object):
    def __init__(self) -> None:
        self._nodes = []
        self._connectors = []

        # scene settings
        self._scene_width = 64000.0
        self._scene_height = 64000.0
        self._editor_scene = EditorScene(self, None)

        # init UI
        self.initUI()

    def initUI(self):
        self._editor_scene.setEditorScene(self._scene_width, self._scene_height)

    def add_node(self, node):
        self._nodes.append(node)

    def add_connector(self, connector):
        self._connectors.append(connector)

    def remove_node(self, node):
        self._nodes.remove(node)

    def remove_connector(self, connector):
        self._connectors.remove(connector)
