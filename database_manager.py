import os
import sqlite3


class DatabaseManager:
    def __init__(self, db_name="library_database.sqlite"):
        """
        Initializes the DatabaseManager and ensures the database exists in the root folder.

        :param db_name: Name of the database file, default is 'library_database.sqlite'.
        """
        # Get the full path to the database file in the root directory
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)

        # Connect to the SQLite database
        self.connection = sqlite3.connect(self.db_path)

        # Create the books table if it doesn't already exist
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            genre TEXT NOT NULL,
            publication_year INTEGER NOT NULL
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def insert_book(self, title, author, isbn, genre, publication_year):
        query = """
        INSERT INTO books (title, author, isbn, genre, publication_year)
        VALUES (?, ?, ?, ?, ?);
        """
        self.connection.execute(query, (title, author, isbn, genre, publication_year))
        self.connection.commit()
        print("Done")

    def fetch_books(self, search_criteria=None):
        query = "SELECT * FROM books"
        if search_criteria:
            query += " WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ? OR genre LIKE ?"
            params = (f"%{search_criteria}%",) * 4
            return self.connection.execute(query, params).fetchall()
        return self.connection.execute(query).fetchall()

    def update_book(self, book_id, title, author, isbn, genre, publication_year):
        query = """
        UPDATE books
        SET title = ?, author = ?, isbn = ?, genre = ?, publication_year = ?
        WHERE id = ?;
        """
        self.connection.execute(query, (title, author, isbn, genre, publication_year, book_id))
        self.connection.commit()

    def delete_book(self, book_id):
        query = "DELETE FROM books WHERE id = ?;"
        self.connection.execute(query, (book_id,))
        self.connection.commit()
