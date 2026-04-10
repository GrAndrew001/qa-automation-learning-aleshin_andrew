from a_expense import Expense

class ExpenseTracker:


    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, description):

        if category == "" or description == "":
            print("Ошибка: категория и описание не могут быть пустыми")
            return False

        if amount <= 0:
            print("Ошибка: сумма должна быть больше 0")
            return False

        expense = Expense(category, amount, description)
        self.expenses.append(expense)
        return True

    def get_all_expenses(self):

        return self.expenses

    def get_total_amount(self):

        total = 0
        for expense in self.expenses:
            total = total + expense.amount
        return total

    def get_expenses_by_category(self, category):

        filtered = []
        total = 0

        for expense in self.expenses:
            if expense.category == category:
                filtered.append(expense)
                total = total + expense.amount

        return filtered, total
