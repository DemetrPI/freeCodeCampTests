class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        # Record a deposit in the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            # Record a withdrawal in the ledger as a negative amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        # Calculate and return the current balance based on the ledger transactions
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            # Perform a transfer between two budget categories, recording transactions in both ledgers
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        # Check if there are sufficient funds for a given amount
        return amount <= self.get_balance()

    def get_withdrawals(self):
        # Calculate and return the total withdrawals (negative amounts) from the ledger
        return sum(item["amount"] for item in self.ledger if item["amount"] < 0)

    def __str__(self):
        lines = []
        total = 0

        for item in self.ledger:
            description = item["description"][:23]
            amount = "{:.2f}".format(item["amount"])
            # Format ledger entries and accumulate the total balance
            lines.append(f"{description}{amount.rjust(30 - len(description))}")
            total += item["amount"]

        title = self.category.center(30, "*")
        lines.append(f"Total: {total:.2f}")
        # Format the category's ledger and total as a string
        return title + "\n" + "\n".join(lines)


def create_spend_chart(categories):
    # Calculate the total spent across all categories (using absolute values for withdrawals)
    total_spent = sum(category.get_withdrawals() for category in categories)

    # Calculate the percentage spent for each category
    percentages = [(category.get_withdrawals() / total_spent) *
                   100 if total_spent != 0 else 0 for category in categories]

    # Initialize the chart string
    chart = "Percentage spent by category\n"

    # Find the maximum name length among categories
    max_name_length = max(len(category.category) for category in categories)

    # Add the vertical bars and labels
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "  # Add 'o' if the percentage is greater than or equal to the current level
            else:
                chart += "   "  # Add spaces if not
        chart += "\n"

    # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"

    max_name_length = max(len(category.category) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "  # Add category name letter by letter
            else:
                chart += "   "  # Add spaces if the category name is shorter
        if i < max_name_length - 1:
            chart += "\n"

    return chart
