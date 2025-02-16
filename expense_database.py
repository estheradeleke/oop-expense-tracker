import uuid
from datetime import datetime, timezone
from expense import Expense  # Import the Expense class

class ExpenseDatabase:
    def __init__(self):
        """Initialize an empty list to store expenses."""
        self.expenses = []

    def add_expense(self, title: str, amount: float):
        """Creates a new Expense and adds it to the list."""
        expense = Expense(title, amount)
        self.expenses.append(expense)
        return expense  # Return the added expense for reference

    def remove_expense(self, expense_id: str):
        """Removes an expense by its ID."""
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        """Retrieves an expense by its ID."""
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if not found

    def get_expenses_by_title(self, title: str):
        """Retrieves all expenses that match a given title."""
        return [exp for exp in self.expenses if exp.title.lower() == title.lower()]

    def to_dict(self):
        """Returns a list of all expenses as dictionaries."""
        return [expense.to_dict() for expense in self.expenses]

# **TEST CODE BELOW**
if __name__ == "__main__":
    db = ExpenseDatabase()

    # Adding expenses
    exp1 = db.add_expense("Groceries", 50.75)
    exp2 = db.add_expense("Rent", 500.00)
    exp3 = db.add_expense("Groceries", 30.25)  # Another grocery expense

    print("All Expenses:", db.to_dict())

    # Fetch expense by ID
    print("Expense by ID:", db.get_expense_by_id(exp1.id).to_dict())

    # Fetch expenses by title
    print("Expenses with title 'Groceries':", [exp.to_dict() for exp in db.get_expenses_by_title("Groceries")])

    # Remove an expense
    db.remove_expense(exp2.id)
    print("Expenses after removal:", db.to_dict())