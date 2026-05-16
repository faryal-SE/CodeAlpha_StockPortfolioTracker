# Stock Portfolio Tracker
# CodeAlpha Internship - Faryal Abro
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420
}

portfolio = {}

print("=" * 40)
print("   STOCK PORTFOLIO TRACKER")
print("=" * 40)
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"  {stock}: ${price}")

print("\nEnter 'done' when finished adding stocks.")

while True:
    stock = input("\nEnter stock name: ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not found! Please choose from the list above.")
        continue
    
    quantity = input(f"Enter quantity of {stock}: ")
    
    if not quantity.isdigit():
        print("Please enter a valid number!")
        continue
    
    quantity = int(quantity)
    
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

if portfolio:
    print("\n" + "=" * 40)
    print("      YOUR PORTFOLIO SUMMARY")
    print("=" * 40)
    total = 0
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total += value
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}")
    print("=" * 40)
    print(f"TOTAL INVESTMENT VALUE: ${total}")
    print("=" * 40)
else:
    print("\nNo stocks added!")
