from library import Library

lib = Library("book.data")

def menu():
    while True:
        print("\n--- Bibliotekssystem ---")
        print("1. Lista alla böcker")
        print("2. Låna en bok")
        print("3. Lämna tillbaka en bok")
        print("4. Inspektera en bok (Baksida)") 
        print("5. Avsluta") 

        choice = input("Välj ett alternativ (1-5): ")

        if choice == "1":
            lib.list_books()

        elif choice == "2":
            lib.borrow_book()
        
        elif choice == "3":
            lib.return_book()

        elif choice == "4":
            lib.inspektera_book()
            
        elif choice == "5":
            print("Programmet avslutas...")
            break

        else:
            print("Ogiltigt val. Vänligen ange en siffra 1-5.")

menu()