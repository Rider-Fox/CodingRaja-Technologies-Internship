# Define classes for expenses and income
class Expense:
  def __init__(self, amount, category):
    self.amount = amount
    self.category = category

class Income:
  def __init__(self, amount, source):
    self.amount = amount
    self.source = source

# Functions to add expense and income
def add_expense():
  try:
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category (e.g., food, rent): ")
    expenses.append(Expense(amount, category))
    print("Expense added successfully!")
  except ValueError:
    print("Invalid amount entered. Please enter a number.")

def add_income():
  try:
    amount = float(input("Enter the income amount: "))
    source = input("Enter the income source (e.g., salary, investment): ")
    income.append(Income(amount, source))
    print("Income added successfully!")
  except ValueError:
    print("Invalid amount entered. Please enter a number.")

# Function to view expenses and income
def view_transactions():
    if not (expenses or income):
        print("No expenses or income added yet.")
    else:
        print("-" * 40)
        print("Transactions:")
        print("-" * 40)
        for transaction in expenses + income:  # Combine both lists
            if isinstance(transaction, Expense):  # Check if it's an Expense
                print(f"Amount: Rs{transaction.amount:.2f} - Category: {transaction.category}")
            else:  # It must be an Income
                print(f"Amount: Rs{transaction.amount:.2f} - Source: {transaction.source}")
        print("-" * 40)


# Function to calculate total expenses, income, and net balance
def calculate_total():
  total_expenses = sum(expense.amount for expense in expenses)
  total_income = sum(income.amount for income in income)
  net_balance = total_income - total_expenses
  print(f"Total expenses: Rs{total_expenses:.2f}")
  print(f"Total income: Rs{total_income:.2f}")
  print(f"Net balance: Rs{net_balance:.2f}")

# Function to save transactions to a file
def save_transactions():
    with open("budget-tracker/transactions.txt", "w") as file:
        for income_transaction in income:
            file.write(f"I {income_transaction.amount} {income_transaction.source}\n")
        for expense_transaction in expenses:
            file.write(f"E {expense_transaction.amount} {expense_transaction.category}\n")

# Function to load transactions from a file
def load_transactions():
    global income, expenses
    income = []
    expenses = []
    try:
        with open("budget-tracker/transactions.txt", "r") as file:
            for line in file:
                transaction_type, amount, description = line.strip().split()
                amount = float(amount)
                if transaction_type == "I":
                    income.append(Income(amount, description))
                elif transaction_type == "E":
                    expenses.append(Expense(amount, description))
    except FileNotFoundError:
        pass

# Initialize empty lists for expenses and income
expenses = []
income = []

# Main loop for user interaction
while True:
  print("\nBudget Tracker")
  print("1. Add expense")
  print("2. Add income")
  print("3. View transactions")
  print("4. Calculate total")
  print("5. Save")
  print("6. Load")
  print("7. Exit")

  choice = input("Enter your choice (1-7): ")

  if choice == "1":
    add_expense()
  elif choice == "2":
    add_income()
  elif choice == "3":
    view_transactions()
  elif choice == "4":
    calculate_total()
  elif choice == "5":
     save_transactions()
  elif choice == "6":
     load_transactions()
  elif choice == "7":
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
