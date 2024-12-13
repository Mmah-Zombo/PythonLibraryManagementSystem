import sys
from PyQt6.QtWidgets import (
    QApplication)
from library import LibraryManagementSystem


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryManagementSystem()
    window.show()
    sys.exit(app.exec())
