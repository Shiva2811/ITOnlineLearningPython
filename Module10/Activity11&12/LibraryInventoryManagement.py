class Book:
    def __init__ (self, title, author,available=True):
        self.title = title
        self.author = author
        self.available = available
    
    def __str__(self):
        return f"'{self.title}' by {self.author}-{'Available' if self.available else 'Not Available'}"
    
class Library:
    def __init__(self):
        #Array to store library's collection of books
        self.books=[]
    
    def add_book(self, title, auther):
        #Adding a new book to the collection
        new_book=Book(title,auther)
        self.books.append(new_book)
        print(f"Book added:{new_book}")
    
    def search_books(self, search_term, by_author=False):
        #searching book my term or auther by using lambda
        if by_author:
            result = list(filter(lambda book:search_term.lower() in book.author.lower(), self.books))
        else:
            result = list(filter(lambda book:search_term.lower() in book.title.lower(), self.books))

        #Display search result
        if result:
            print("Search results : ")
            for book in result:
                print(book)
        else:
            print("no book found")
        
    def update_availability(self, title, availability):
        #update the availability of a book with a specific title using lambda
        book = next((b for b in self.books if b.title.lower()==title.lower()), None)
        if book:
            book.available = availability
            print(f"Updated availability : {book}")
        else:
            print(f"Book titled {title} not found in library")

#Test the functionality
library = Library() 

# Add books to the library
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

# Search for books by title
library.search_books("1984")

# Search for books by author
library.search_books("George Orwell", by_author=True)

# Update book availability
library.update_availability("The Great Gatsby", False)

# Verify updated availability
library.search_books("The Great Gatsby")