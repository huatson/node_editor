"""
Node Editor Sample
"""

import sys
from PyQt5.QtWidgets import QApplication
from node_editor.window import NodeEditorWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NodeEditorWindow()
    sys.exit(app.exec_())
