from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QSpinBox, QPushButton, QHBoxLayout)


class AddBookDialog(QDialog):
    def __init__(self, parent=None):
        """
        Dialog for adding a new book to the library.
        """
        super().__init__(parent)
        self.setWindowTitle("Add New Book")
        self.setMinimumSize(400, 300)

        # Main layout
        self.layout = QVBoxLayout(self)

        # Form layout
        self.form_layout = QFormLayout()

        # Input fields
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter book title")
        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Enter author's name")
        self.isbn_input = QLineEdit()
        self.isbn_input.setPlaceholderText("Enter ISBN (unique)")
        self.genre_input = QComboBox()
        self.genre_input.addItems(["Fiction", "Non-Fiction", "Science", "History", "Biography", "Other"])
        self.year_input = QSpinBox()
        self.year_input.setRange(1900, 2100)
        self.year_input.setValue(2023)

        # Add fields to form layout
        self.form_layout.addRow("Title:", self.title_input)
        self.form_layout.addRow("Author:", self.author_input)
        self.form_layout.addRow("ISBN:", self.isbn_input)
        self.form_layout.addRow("Genre:", self.genre_input)
        self.form_layout.addRow("Publication Year:", self.year_input)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.cancel_button)

        # Add layouts to main layout
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.button_layout)

    def get_book_details(self):
        """
        Retrieve the entered book details.
        :return: A dictionary containing book details.
        """
        return {
            "title": self.title_input.text(),
            "author": self.author_input.text(),
            "isbn": self.isbn_input.text(),
            "genre": self.genre_input.currentText(),
            "year": self.year_input.value()
        }
