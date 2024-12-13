import sys
from PyQt6.QtWidgets import (
    QApplication, QDialog
)

from book_details import BookDetailsDialog
from library import LibraryManagementSystem
from PyQt6.QtCore import Qt


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryManagementSystem()
    window.show()
    sys.exit(app.exec())
