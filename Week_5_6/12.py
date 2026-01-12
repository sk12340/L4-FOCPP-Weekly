class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"

class Library:
    def __init__(self):
        self.books = []
        self.load_books()
    
    def load_books(self):
        try:
            with open("books.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        b = Book(parts[0], parts[1], parts[2])
                        b.issued = parts[3] == 'True'
                        self.books.append(b)
        except FileNotFoundError:
            print("No book file found. Starting fresh.")
    
    def save_books(self):
        with open("books.txt", "w") as f:
            for book in self.books:
                f.write(f"{book.book_id},{book.title},{book.author},{book.issued}\n")
    
    def add_book(self):
        bid = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(bid, title, author))
        self.save_books()
        print("Book added.")
    
    def issue_book(self):
        bid = input("Enter Book ID to issue: ")
        for book in self.books:
            if book.book_id == bid:
                if book.issued:
                    print("Book already issued.")
                else:
                    book.issued = True
                    print("Book issued.")
                self.save_books()
                return
        print("Book not found.")
    
    def return_book(self):
        bid = input("Enter Book ID to return: ")
        for book in self.books:
            if book.book_id == bid:
                if book.issued:
                    book.issued = False
                    print("Book returned.")
                else:
                    print("Book was not issued.")
                self.save_books()
                return
        print("Book not found.")
    
    def search_book(self):
        term = input("Enter title or author to search: ")
        found = False
        for book in self.books:
            if term.lower() in book.title.lower() or term.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No matching books.")
    
    def show_all(self):
        if not self.books:
            print("No books.")
        else:
            for book in self.books:
                print(book)

lib = Library()
while True:
    print("\n1. Add Book\n2. Issue Book\n3. Return Book\n4. Search Book\n5. Show All\n6. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        lib.add_book()
    elif ch == '2':
        lib.issue_book()
    elif ch == '3':
        lib.return_book()
    elif ch == '4':
        lib.search_book()
    elif ch == '5':
        lib.show_all()
    elif ch == '6':
        break
    else:
        print("Invalid choice.")