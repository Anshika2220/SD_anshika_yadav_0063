from shop import BookShop


shop = BookShop()

while True:
    print("\n========== BOOK SHOP ==========")
    print("1. Display Books")
    print("2. Buy Book")
    print("3. Show Shop Savings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        shop.display_books()

    elif choice == "2":
        shop.buy_book()

    elif choice == "3":
        shop.show_savings()

    elif choice == "4":
        print("Thank You for Visiting!")
        break

    else:
        print("Invalid Choice!")