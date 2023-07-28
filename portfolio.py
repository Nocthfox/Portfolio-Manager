class Portfolio:
    def __init__(self):
        self.holdings = {}

    def add_holding(self, symbol, quantity, purchase_price):
        if symbol in self.holdings:
            print("Holding already exists. Use update_holding() to modify.")
        else:
            self.holdings[symbol] = {
                'quantity': quantity,
                'purchase_price': purchase_price
            }
            print(f"{symbol} holding added successfully.")

    def update_holding(self, symbol, quantity, purchase_price):
        if symbol in self.holdings:
            self.holdings[symbol]['quantity'] = quantity
            self.holdings[symbol]['purchase_price'] = purchase_price
            print(f"{symbol} holding updated successfully.")
        else:
            print("Holding does not exist. Use add_holding() to add a new holding.")

    def remove_holding(self, symbol):
        if symbol in self.holdings:
            del self.holdings[symbol]
            print(f"{symbol} holding removed successfully.")
        else:
            print("Holding does not exist.")

    def calculate_profit_loss(self, symbol, current_price):
        if symbol in self.holdings:
            holding = self.holdings[symbol]
            purchase_price = holding['purchase_price']
            quantity = holding['quantity']
            profit_loss = (current_price - purchase_price) * quantity
            return profit_loss
        else:
            print("Holding does not exist.")
            return None

    def generate_portfolio_report(self, current_prices):
        total_portfolio_value = 0
        print("Portfolio Report:")
        print("-----------------")
        for symbol, holding in self.holdings.items():
            quantity = holding['quantity']
            purchase_price = holding['purchase_price']
            if symbol in current_prices:
                current_price = current_prices[symbol]
                holding_value = current_price * quantity
                profit_loss = self.calculate_profit_loss(symbol, current_price)
                total_portfolio_value += holding_value
                print(f"Symbol: {symbol}")
                print(f"Quantity: {quantity}")
                print(f"Purchase Price: ${purchase_price}")
                print(f"Current Price: ${current_price}")
                print(f"Holding Value: ${holding_value}")
                print(f"Profit/Loss: ${profit_loss}")
                print("-----------------")
            else:
                print(f"Could not fetch price for {symbol}")

        print(f"Total Portfolio Value: ${total_portfolio_value}")


# Example usage:
portfolio = Portfolio()

# Add holdings:
portfolio.add_holding("BTC", 1.5, 35000)
portfolio.add_holding("ETH", 5, 2000)

# Update a holding:
portfolio.update_holding("ETH", 7, 2200)

# Remove a holding
portfolio.remove_holding("BTC")

# Calculate profit/loss for a holding
current_prices = {
    "BTC": 38000,
    "ETH": 2300
}
profit_loss = portfolio.calculate_profit_loss("ETH", current_prices["ETH"])
print(f"Profit/Loss for ETH: ${profit_loss}")

# Generate portfolio report
portfolio.generate_portfolio_report(current_prices)
