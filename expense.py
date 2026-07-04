users = {}

# Add Expense
def add_expense():
    name = input("Enter User Name: ")

    if name not in users:
        users[name] = []

    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount: ₹"))

    expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    users[name].append(expense)

    print("\nExpense Added Successfully!\n")


# View Expenses
def view_expenses():
    name = input("Enter User Name: ")

    if name not in users or len(users[name]) == 0:
        print("\nNo expenses found for this user.\n")
        return

    total = 0

    print(f"\n----- Expenses of {name} -----")

    for i, expense in enumerate(users[name], start=1):
        print(f"\nExpense {i}")
        print("Date       :", expense["Date"])
        print("Category   :", expense["Category"])
        print("Description:", expense["Description"])
        print("Amount     : ₹", expense["Amount"])

        total += expense["Amount"]

    print("\nTotal Expense: ₹", total)
    print()


# Main Menu
while True:
    print("====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")