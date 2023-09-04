"""
Node Editor Sample
"""

from node_editor.window import NodeEditorWindow
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NodeEditorWindow()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
