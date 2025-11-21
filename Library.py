from Book import Book

class Library: 
    
    def __init__(self, filename): 
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self): #läser böcker från filen
        with open(self.filename, "r") as f:
            for line in f.readlines():
                title, author, borrowed = line.strip().split(", ")
                
                # Gör om borrowed från text -> bool
                borrowed = borrowed == "1"
                
                self.books.append(Book(title, author, borrowed))

    def save_books(self):
        with open(self.filename, "w") as f:
            for book in self.books:
                f.write(book.to_file_line() + "\n")

    def list_books(self):
        print("\nAlla böcker:")
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book}")
