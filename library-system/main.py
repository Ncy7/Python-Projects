from book import Book
from library import Library

def main():
    library = Library()
    library.load_from_file()
    
    while True:
        print("\n" + "="*50)
        print("   Library Management System")
        print("="*50)
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Quit")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            isbn = input("Enter ISBN: ").strip()
            if title and author and isbn:
                book = Book(title, author, isbn)
                library.add_book(book)
            else:
                print("All fields are required!")
        
        elif choice == "2":
            library.view_all_books()
        
        elif choice == "3":
            title = input("Enter title to search: ").strip()
            book = library.find_book_by_title(title)
            if book:
                print(f"\nFound: {book}")
            else:
                print("Book not found.")
        
        elif choice == "4":
            title = input("Enter title to borrow: ").strip()
            library.borrow_book(title)
        
        elif choice == "5":
            title = input("Enter title to return: ").strip()
            library.return_book(title)
        
        elif choice == "6":
            library.save_to_file() 
            print("Thank you for using the Library System. Goodbye! 👋")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()