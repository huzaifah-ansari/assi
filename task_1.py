class Book:

    def __init__(self, title: str, author: str, isbn: str):
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  

    def display_info(self):
      
        status = "Checked out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")

    def check_out(self):
        
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def check_in(self):
      
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been checked in.")
        else:
            print(f"'{self.title}' is already available.")

class library:

    def __init__(self,name:str):
        self.name=name
        self.books=[]
    
    def add_book(self, book_object):
         self.books.append(book_object)
         print(f"'{book_object.title }' added to {self.name}.")

    def find_book_by_title(self, title:str):
        for book in self.books:
            if book.title ==title:
                return book
            
        print(f"Book with title '{title}' not found.")
        return None

    def check_out_book(self, title:str):
        book_to_check_out = self.find_book_by_title(title)

        if book_to_check_out:
            book_to_check_out.check_out()

    def check_in_book(self, title:str):
        book_to_check_in = self.find_book_by_title(title)
        if book_to_check_in:
            book_to_check_in.check_in()

    def list_available_books(self):

        print(f"Available books in {self.name}:")

        available_count = 0
        for book in self.books:
            if not book.is_checked_out:
                book.display_info()
                print("-" * 20) 
                available_count += 1

        if available_count == 0:
            print("No books currently available.")
    
    def list_all_books(self):
        
        print(f"All books in {self.name}:")
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            book.display_info()
            print("-" * 20)

                
                    #Testing 


book1 = Book("Python for Beginners", "John Coder", "1234567890") 
book2 = Book("Advanced OOP Concepts", "Jane Hacker", "0987654321") 
book3 = Book("Data Structures in Python", "Alan Turing Jr.", "1122334455") 

my_library =library("Downtown Coding Library")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

print("-" * 20)

my_library.list_available_books() 
print("-" * 20)

my_library.check_out_book("Python for Beginners") 
print("-" * 20) 

my_library.check_out_book("Python for Beginners") 
print("-" * 20) 

my_library.list_available_books() 
print("-" * 20)

my_library.check_in_book("Python for Beginners") 
print("-" * 20)

my_library.check_in_book("Advanced OOP Concepts")
print("-" * 20)

my_library.list_all_books()