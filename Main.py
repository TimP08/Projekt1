from library import Library

lib = Library("book_data.txt")

def menu():
    while True:
        print("\n--- Bibliotekssystem ---")
        print("1. Lista alla böcker")
        print("2. Låna en bok")
        print("3. Lämna tillbaka en bok")
        print("4. Avsluta")

        choice = input("Välj ett alternativ (1-4): ")

        if choice == "1":
            lib.list_books()

        elif choice == "2":
            lib.borrow_book()

        elif choice == "3":
            lib.return_book()

        elif choice == "4":
            print("Programmet avslutas...")
            break

        else:
            print("Fel val! Försök igen.")

menu()
