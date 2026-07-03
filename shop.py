from Book import Book


class BookShop:
    def __init__(self):
        self.books = [
            Book(1, "Harry Potter", 500, 10),
            Book(2, "Good girls guide to murder", 650, 8),
            Book(3, "The Inheritance Game ", 700, 5),
            Book(4, "The Cruel Prince", 600, 6),
            Book(5, "The Reappearance Of Rachel Price", 750, 4)
        ]
        self.savings = 0

    def display_books(self):
        print("\n========== AVAILABLE BOOKS ==========")
        print(f"{'ID':<5}{'Title':<40}{'Price':<10}{'Stock'}")
        print("-" * 50)

        for book in self.books:
            print(f"{book.book_id:<5}{book.title:<}₹{book.price:<9}{book.stock}")

    def buy_book(self):
        customer = input("\nEnter Customer Name: ")
        book_id = int(input("Enter Book ID: "))
        quantity = int(input("Enter Quantity: "))

        for book in self.books:
            if book.book_id == book_id:

                if quantity <= book.stock:

                    total = book.price * quantity
                    book.stock -= quantity
                    self.savings += total

                    # Generate Bill
                    print("\n")
                    print("=" * 40)
                    print("           BOOK SHOP BILL")
                    print("=" * 40)
                    print(f"Customer Name : {customer}")
                    print(f"Book Name     : {book.title}")
                    print(f"Price         : ₹{book.price}")
                    print(f"Quantity      : {quantity}")
                    print("-" * 40)
                    print(f"Total Amount  : ₹{total}")
                    print("=" * 40)
                    print("Thank you for shopping!")
                    print("=" * 40)

                else:
                    print("Sorry! Book is out of stock.")

                return

        print("Book ID not found.")

    def show_savings(self):
        print(f"\nTotal Shop Savings: ₹{self.savings}")