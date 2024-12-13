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

# if __name__ == "__main__":
#     import sys
#     from PyQt6.QtWidgets import QApplication
#
#     app = QApplication(sys.argv)
#
#     dialog = BookDetailsDialog()
#     result = dialog.exec()
#     print("Dialog result:", result)
#
#     if result == QDialog.DialogCode.Accepted:
#         print("Dialog was accepted")
#         print("Book details:", dialog.get_book_details())
#     else:
#         print("Dialog was canceled.")
