# Library Management System

A desktop application for managing library books built using PyQt6 for the user interface and SQLite for the database. The system allows users to perform CRUD operations (Create, Read, Update, Delete) on book records and is designed for ease of use and maintainability.

## Features
### 1.	Book Management:

| Operation    | Description                                                                  |
|--------------|------------------------------------------------------------------------------|
| Add Books    | Enter book details such as title, author, ISBN, genre, and publication year. |
| View Books   | Display all books in a table with search and filter functionality.           |
| Update Books | Modify details of existing books.                                            |
| Delete Books | Remove books from the database.                                              |
| Search Books | Find books based on title, author, ISBN, genre, and publication year         |

### 2.	Database:
1. Powered by SQLite.
2. Ensures data persistence and supports multiple book records.

### 3.	User Interface:
1. Designed with PyQt6.
2. Includes intuitive dialogs for adding and updating books.
	
### 4.	Validation:
1. Ensures unique ISBNs for books.
2. Handles missing or invalid data gracefully.

## Requirements
	• Python 3.8 or higher
	• PyQt6
	• SQLite3 (comes pre-installed with Python)

## Installation
1. Clone the repository:

```commandline
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

2. Install dependencies:

```commandline
pip install PyQt6
```

3. Run the application:

```commandline
python main.py
```

## Usage
1. Add a Book:
   1. Click the “Add Book” button.
   2. Fill in the book details (title, author, ISBN, genre, publication year) in the dialog.
   3. Click “Save” to add the book.
2. Search and View Books:
   1. Use the search bar to filter books by title, author, ISBN, or genre.
   2. The table dynamically updates based on your search criteria.
3. Update a Book:
   1. Select a book from the table.
   2. Click the “Update Book” button.
   3. Modify the book details in the dialog and click “Save.”
4. Delete a Book:
   1. Select a book from the table.
   2. Click the “Delete Book” button to remove it from the database.

## Project Structure

```
library-management-system/
│
├── main.py                 # Main entry point for the application
├── library.py              # Core application logic (UI and functionality)
├── database_manager.py     # Database handling logic (CRUD operations)
├── BookDetailsDialog.py    # Dialog for adding/updating book details
├── library_database.sqlite # SQLite database file (created automatically)
└── README.md               # Project documentation
```


## Technical Details

### 1. Database

The database `library_database.sqlite` is automatically created in the root directory. It contains a single table, books, with the following schema:

```SQL
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT UNIQUE NOT NULL,
    genre TEXT NOT NULL,
    publication_year INTEGER NOT NULL
);
```


### 2. PyQt6

The user interface is built using PyQt6, featuring:

1. QMainWindow: Main application window.
2. TableWidget: Displays book records in a tabular format.
3. Dialog: Used for adding and updating books.
4. QMessageBox: Provides error and success notifications.

## Contributing
1. Fork the repository.
2. Create a new branch:

```commandline
git checkout -b feature-name
```

3. Commit your changes:

```commandline
git commit -m "Add your message"
```

4. Push to your branch:

```commandline
git push origin feature-name
```
5.	Open a pull request.

## Future Enhancements
1. Add user authentication and roles (admin, librarian, etc.).
2. Implement functionality to track book lending/borrowing.
3. Provide export/import functionality for book data.

## Team

1. Mustapha Pabai
2. Patrick Majid Kawa
3. M'mah Zombo

## Acknowledgments

This application was developed as part of a group project for Limkokwing University, showcasing:
1. Object-Oriented Programming (OOP) principles.
2. PyQt for GUI design.
3. SQLite for database management.
