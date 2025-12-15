import json
import os
from book import Book

DATA_FILE = "data/books.json"
DATA_DIR = "data"

class Library:

    def __init__(self):
        self.books = [] # List to store Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def borrow_book(self, title):
        book = self.find_book_by_title(title)
        if book:
            book.borrow()
        else:
            print(f"Book '{title}' not found in the library.")
    
    def return_book(self, title):
        book = self.find_book_by_title(title)
        if book:
            book.return_book()
        else:
            print(f"Book '{title}' not found in the library.")

    def view_all_books(self):
        if not self.books:
            print("No books in the library yet.")
            return
        
        print("\n" + "="*50)
        print("All Books in the Library")
        print("="*50)
        for book in self.books:
            print(book)
        print("="*50)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def save_to_file(self):
        # Create data directory if it doesn't exist
        os.makedirs(DATA_DIR, exist_ok=True)
        
        # Convert books to simple dictionaries
        books_data = [
            {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "is_borrowed": book.is_borrowed
            }
            for book in self.books
        ]
        
        with open(DATA_FILE, "w") as f:
            json.dump(books_data, f, indent=4)
        print("Library saved to file.")

    def load_from_file(self):
        if not os.path.exists(DATA_FILE):
            print("No saved library found. Starting fresh.")
            return
        
        try:
            with open(DATA_FILE, "r") as f:
                books_data = json.load(f)
            
            self.books = []  # Clear current books
            for data in books_data:
                book = Book(data["title"], data["author"], data["isbn"])
                book.is_borrowed = data["is_borrowed"]
                self.books.append(book)
            print(f"Loaded {len(self.books)} books from file.")
        except Exception as e:
            print(f"Error loading file: {e}")