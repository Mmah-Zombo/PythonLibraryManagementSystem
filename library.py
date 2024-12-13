from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QDialog, QMessageBox, QWidget)
from database_manager import DatabaseManager
import sqlite3
from book_details import BookDetailsDialog
from book_dialog import BookDialog


class LibraryManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.setGeometry(200, 200, 800, 600)

        # Database Manager
        self.db_manager = DatabaseManager()

        # Main Widget
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search books...")
        self.search_bar.textChanged.connect(self.load_books)
        self.layout.addWidget(self.search_bar)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Author", "ISBN", "Genre", "Year"])
        self.layout.addWidget(self.table)

        # Buttons
        self.add_button = QPushButton("Add Book")
        self.update_button = QPushButton("Update Book")
        self.delete_button = QPushButton("Delete Book")

        self.add_button.clicked.connect(self.open_add_book_dialog)
        self.update_button.clicked.connect(self.open_update_book_dialog)
        self.delete_button.clicked.connect(self.delete_book)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.update_button)
        self.layout.addWidget(self.delete_button)

        # Set Layout
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        # Load books on start
        self.load_books()

    def load_books(self):
        """Load books from the database and populate the table."""
        search_text = self.search_bar.text()
        books = self.db_manager.fetch_books(search_text)

        self.table.setRowCount(len(books))
        for row_idx, book in enumerate(books):
            for col_idx, data in enumerate(book):
                if data is not None:  # Prevent None values
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def open_add_book_dialog(self):
        """Open the Add Book dialog to enter book details."""
        dialog = BookDetailsDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            book_details = dialog.get_book_details()
            # Save to database
            try:
                self.db_manager.insert_book(
                    book_details["title"],
                    book_details["author"],
                    book_details["isbn"],
                    book_details["genre"],
                    book_details["year"]
                )
                QMessageBox.information(self, "Success", "Book added successfully!")
                self.load_books()  # Refresh table
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Error", "ISBN must be unique. Please try again.")

    def open_update_book_dialog(self):
        """Open the update book dialog with pre-filled data."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a book to update.")
            return

        book_id = int(self.table.item(selected_row, 0).text())
        title = self.table.item(selected_row, 1).text()
        author = self.table.item(selected_row, 2).text()
        isbn = self.table.item(selected_row, 3).text()
        genre = self.table.item(selected_row, 4).text()
        print(self.table.item(selected_row, 5))
        year = int(self.table.item(selected_row, 5).text())

        dialog = BookDialog(self, (title, author, isbn, genre, year))
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            self.db_manager.update_book(book_id, *data)
            self.load_books()

    def delete_book(self):
        """Delete the selected book."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a book to delete.")
            return

        book_id = int(self.table.item(selected_row, 0).text())
        self.db_manager.delete_book(book_id)
        self.load_books()
