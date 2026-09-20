# Stock Portfolio Tracker

portfolio = []


def add_stock():
    name = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    buy_price = float(input("Enter buy price per share: "))

    stock = {
        "name": name,
        "quantity": quantity,
        "buy_price": buy_price
    }

    portfolio.append(stock)
    print("\nStock added successfully!")


def view_portfolio():
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n========== STOCK PORTFOLIO ==========")

    total_investment = 0

    for stock in portfolio:
        investment = stock["quantity"] * stock["buy_price"]
        total_investment += investment

        print(f"\nStock Name : {stock['name']}")
        print(f"Quantity   : {stock['quantity']}")
        print(f"Buy Price  : ₹{stock['buy_price']:.2f}")
        print(f"Investment : ₹{investment:.2f}")

    print("\n-------------------------------------")
    print(f"Total Investment: ₹{total_investment:.2f}")


def remove_stock():
    name = input("Enter stock name to remove: ")

    for stock in portfolio:
        if stock["name"].lower() == name.lower():
            portfolio.remove(stock)
            print("\nStock removed successfully!")
            return

    print("\nStock not found.")


while True:
    print("\n========== STOCK PORTFOLIO TRACKER ==========")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Remove Stock")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_stock()

    elif choice == "2":
        view_portfolio()

    elif choice == "3":
        remove_stock()

    elif choice == "4":
        print("\nThank you for using Stock Portfolio Tracker!")
        break

    else:
        print("\nInvalid choice. Please try again.")