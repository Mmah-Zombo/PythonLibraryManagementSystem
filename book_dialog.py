import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QLineEdit, QFormLayout, QDialog, QLabel, QSpinBox, QComboBox, QHBoxLayout, QMessageBox, QWidget
)
from PyQt6.QtCore import Qt


class BookDialog(QDialog):
    def __init__(self, parent=None, book_data=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Book")
        self.layout = QFormLayout()

        # Fields
        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.isbn_input = QLineEdit()
        self.genre_input = QComboBox()
        self.genre_input.addItems(["Fiction", "Non-Fiction", "Science", "History", "Biography"])
        self.year_input = QSpinBox()
        self.year_input.setRange(1900, 2100)

        # Prefill data if available
        if book_data:
            self.title_input.setText(book_data[0])
            self.author_input.setText(book_data[1])
            self.isbn_input.setText(book_data[2])
            self.genre_input.setCurrentText(book_data[3])
            self.year_input.setValue(book_data[4])

        # Add fields to layout
        self.layout.addRow("Title:", self.title_input)
        self.layout.addRow("Author:", self.author_input)
        self.layout.addRow("ISBN:", self.isbn_input)
        self.layout.addRow("Genre:", self.genre_input)
        self.layout.addRow("Year:", self.year_input)

        # Buttons
        self.button_box = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.button_box.addWidget(self.save_button)
        self.button_box.addWidget(self.cancel_button)

        self.layout.addRow(self.button_box)
        self.setLayout(self.layout)

    def get_data(self):
        """Get book data from the dialog."""
        return (
            self.title_input.text(),
            self.author_input.text(),
            self.isbn_input.text(),
            self.genre_input.currentText(),
            self.year_input.value(),
        )

