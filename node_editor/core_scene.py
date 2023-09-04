from node_editor.editor_scene import NodeEditorScene

class Scene(object):
    def __init__(self) -> None:
        self._nodes = []
        self._edges = []

        self._scene_width = 64000.0
        self._scene_height = 64000.0

        self._editor_scene = None

        self.init_ui()

    def init_ui(self):
        self._editor_scene = NodeEditorScene(self, None)
        self._editor_scene.setGraphicsScene(self._scene_width, self._scene_height)

    def add_node(self, node):
        self._nodes.append(node)

    def add_edge(self, edge):
        self._edges.append(edge)

    def remove_node(self, node):
        self._nodes.remove(node)

    def remove_edge(self, edge):
        self._edges.remove(edge)