class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
            return False
        else:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
            return True

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
            return False
        else:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
            return True

    def __str__(self):
        # This controls how the book looks when printed
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"