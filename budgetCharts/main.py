# Import necessary modules from the budget package
import budget
from budget import create_spend_chart
from unittest import main

# Create a 'Food' category
food = budget.Category("Food")
# Perform initial deposit and withdrawals
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# Print the current balance of the 'Food' category
print(food.get_balance())

# Create a 'Clothing' category
clothing = budget.Category("Clothing")
# Transfer funds from 'Food' to 'Clothing' category
food.transfer(50, clothing)
# Perform withdrawals in the 'Clothing' category
clothing.withdraw(25.55)
clothing.withdraw(100)

# Create an 'Auto' category
auto = budget.Category("Auto")
# Perform initial deposit and a withdrawal
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# Print the details of the 'Food' and 'Clothing' categories
print(food)
print(clothing)

# Generate and print a spend chart for the categories 'Food', 'Clothing', and 'Auto'
print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically using the 'test_module'
main(module='test_module', exit=False)
