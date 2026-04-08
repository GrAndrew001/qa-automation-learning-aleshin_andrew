

class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description

    def show(self):
        """Показать один расход"""
        print(f"{self.category} | {self.amount} руб. | {self.description}")