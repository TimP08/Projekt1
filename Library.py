from Book import Book

class Library: 
    
    def __init__(self, filename): 
        self.filename = filename
        self.books = []
        self.load_books()

    # Läser in böcker från filen
    def load_books(self):
        with open(self.filename, "r") as f:
            for line in f.readlines():
                title, author, borrowed = line.strip().split(", ")
                
                # Gör om borrowed från text -> bool
                borrowed = borrowed == "1"
                
                self.books.append(Book(title, author, borrowed))

    # Sparar alla böcker till filen
    def save_books(self):
        with open(self.filename, "w") as f:
            for book in self.books:
                f.write(book.to_file_line() + "\n")

    # Skriver ut alla böcker
    def list_books(self):
        print("\nAlla böcker:")
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book}")

    # Skriver ut utlånade böcker  
    def list_borrowed_books(self):
        print("\nUtlånade böcker:")
        borrowed_books = [book for book in self.books if book.borrowed]

        if not borrowed_books:
            print("Inga böcker är utlånade.")
            return None

        for i, book in enumerate(borrowed_books):
            print(f"{i+1}. {book}")

        return borrowed_books

    # Skriver ut lediga böcker
    def list_available_books(self):
        print("\nLediga böcker:")
        available_books = [book for book in self.books if not book.borrowed]
    
        if not available_books:
            print("Inga böcker finns tillgängliga just nu.")
            return None
        
        for i, book in enumerate(available_books):
            print(f"{i+1}. {book}")

        return available_books

    # Lånar bok
    def borrow_book(self):
        self.list_available_books()
        choice = input("\nVilken bok vill du låna? (nummer): ")

        if not choice.isdigit():
            print("Du måste skriva ett nummer.")
            return
        
        choice = int(choice) - 1

        if choice < 0 or choice >= len(self.books):
            print("Ogiltigt val.")
            return

        book = self.books[choice]

        if book.borrowed:
            print("Boken är redan utlånad.")
        else:
            book.borrowed = True
            self.save_books()
            print(f"Du har nu lånat '{book.title}'.")

    # Lämnar tillbaka bok
    def return_book(self):
        self.list_borrowed_books()
        choice = input("\nVilken bok vill du lämna tillbaka? (nummer): ")

        if not choice.isdigit():
            print("Du måste skriva ett nummer.")
            return
        
        choice = int(choice) - 1

        if choice < 0 or choice >= len(self.books):
            print("Ogiltigt val.")
            return

        book = self.books[choice]

        if not book.borrowed:
            print("Denna bok är inte utlånad.")
        else:
            book.borrowed = False
            self.save_books()
            print(f"Du har nu lämnat tillbaka '{book.title}'.")    
    
    def inspect_book(self):
        print("\nVälj en bok att inspektera:")
        self.list_available_books()

        choice = input("\nVilken bok vill du inspektera? (nummer): ")

        # Kontrollera att det är ett nummer
        if not choice.isdigit():
            print("Du måste skriva ett nummer.")
            return
        
        choice = int(choice) - 1

        # Kontrollera att numret finns
        if choice < 0 or choice >= len(self.books):
            print("Ogiltigt val.")
            return

        book = self.books[choice]

        # Försök läsa baksidorna
        try:
            with open("bookdescriptions.txt", "r", encoding="utf-8") as f:
                descriptions = f.readlines()
        except FileNotFoundError:
            print("Filen 'bookdescriptions.txt' kunde inte hittas!")
            return

        # Om filen är tom eller saknar beskrivning på rätt rad
        if choice >= len(descriptions):
            print(f"\nIngen baksidetext finns för '{book.title}'.")
            return

        description = descriptions[choice].strip()

        if description == "":
            print(f"\nIngen baksidetext finns för '{book.title}'.")
        else:
            print(f"\n--- Baksidetext för '{book.title}' ---")
            print(description)
            print("--------------------------------------")