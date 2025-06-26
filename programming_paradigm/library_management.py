class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out
    
    def checked_out(self):
        self._is_checked_out = True
    
    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.checked_out()
                print(f"checked out '{title}'")
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"returned '{title}'")
                return
        print(f"Book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        book_list = [book for book in self._books if book.is_available()]
        if not book_list:
            print("No books are currently available.")
        else:
            for book in book_list: 
                print(f"{book.title} {book.author}")


