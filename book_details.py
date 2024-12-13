from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QComboBox, QSpinBox, QPushButton, QHBoxLayout


class BookDetailsDialog(QDialog):
    def __init__(self, parent=None, book_data=None):
        """
        Dialog to add or edit book details.

        :param parent: The parent window of the dialog.
        :param book_data: Tuple containing book details for editing (optional).
        """
        super().__init__(parent)
        self.setWindowTitle("Book Details")
        self.setMinimumSize(400, 300)

        # Layout for form inputs
        self.layout = QFormLayout(self)

        # Input fields
        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.isbn_input = QLineEdit()
        self.genre_input = QComboBox()
        self.genre_input.addItems(["Fiction", "Non-Fiction", "Science", "History", "Biography", "Other"])
        self.year_input = QSpinBox()
        self.year_input.setRange(1900, 2100)
        self.year_input.setValue(2023)

        # Prefill fields if book_data is provided
        if book_data:
            self.title_input.setText(book_data.get("title", ""))
            self.author_input.setText(book_data.get("author", ""))
            self.isbn_input.setText(book_data.get("isbn", ""))
            self.genre_input.setCurrentText(book_data.get("genre", "Fiction"))
            self.year_input.setValue(book_data.get("year", 2023))

        # Add fields to layout
        self.layout.addRow("Title:", self.title_input)
        self.layout.addRow("Author:", self.author_input)
        self.layout.addRow("ISBN:", self.isbn_input)
        self.layout.addRow("Genre:", self.genre_input)
        self.layout.addRow("Year:", self.year_input)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.cancel_button)

        # Add buttons to the layout
        self.layout.addRow(self.button_layout)

    def get_book_details(self):
        """
        Retrieve the entered book details as a dictionary.
        """
        return {
            "title": self.title_input.text(),
            "author": self.author_input.text(),
            "isbn": self.isbn_input.text(),
            "genre": self.genre_input.currentText(),
            "year": self.year_input.value()
        }
