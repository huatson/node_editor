"""
Node Editor Sample
"""

from node_editor.editor_window import EditorWindow
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorWindow(app, None)
    window.raise_()
    sys.exit(app.exec_())
