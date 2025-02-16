
import uuid
from datetime import datetime,timezone

class Expense:
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)  # Set creation timestamp
        self.updated_at = self.created_at  # Initially same as created_at

    def update(self, title: str = None, amount: float = None):
        """Updates the expense's title and/or amount."""
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)  # Update the timestamp

    def to_dict(self):
        """Returns a dictionary representation of the expense."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

# **TEST CODE BELOW**
if __name__ == "__main__":
    expense = Expense("Groceries", 50.75)  # Create an instance of Expense
    print(expense.to_dict())  # Print the expense as a dictionary