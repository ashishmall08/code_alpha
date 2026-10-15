# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

print("===== STOCK PORTFOLIO TRACKER =====")

total_investment = 0
portfolio = []

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        portfolio.append({
            "stock": stock,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        print(f"{stock} added successfully.")
        print(f"Price per share: ${price}")
        print(f"Investment: ${investment}")

    except ValueError:
        print("Please enter a valid quantity.")


# Display portfolio
print("\n========== PORTFOLIO ==========")

if len(portfolio) == 0:
    print("No stocks were added.")

else:
    print("Stock\tQuantity\tPrice\tInvestment")

    for item in portfolio:
        print(
            f"{item['stock']}\t"
            f"{item['quantity']}\t\t"
            f"${item['price']}\t"
            f"${item['investment']}"
        )

    print("--------------------------------")
    print(f"Total Investment: ${total_investment}")


# Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:

        file.write("===== STOCK PORTFOLIO =====\n\n")

        for item in portfolio:
            file.write(
                f"Stock: {item['stock']}\n"
                f"Quantity: {item['quantity']}\n"
                f"Price: ${item['price']}\n"
                f"Investment: ${item['investment']}\n\n"
            )

        file.write("--------------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Portfolio saved successfully in portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker!")