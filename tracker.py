
from expense import Expense


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        print("Добавление расхода")

        # Категория
        category = input("Категория: ")
        while category == "":
            print("Ошибка: категория не может быть пустой")
            category = input("Категория: ")

        # Сумма
        amount = input("Сумма: ")
        while not amount.isdigit():
            print("Ошибка: введите число")
            amount = input("Сумма: ")
        amount = int(amount)

        while amount <= 0:
            print("Ошибка: сумма должна быть больше 0")
            amount = int(input("Сумма: "))

        # Описание
        description = input("Описание: ")
        while description == "":
            print("Ошибка: описание не может быть пустым")
            description = input("Описание: ")

        # Сохранить
        new_expense = Expense(category, amount, description)
        self.expenses.append(new_expense)
        print("Расход добавлен.")

    def show_all(self):
        print("Все расходы")

        if len(self.expenses) == 0:
            print("Нет записей")
            return

        total = 0
        for i in range(len(self.expenses)):
            exp = self.expenses[i]
            print(f"{i + 1}. {exp.category} | {exp.amount} руб. | {exp.description}")
            total = total + exp.amount

        print(f"\nОбщая сумма: {total} руб.")

    def show_by_category(self):
        print("Расходы по категории")

        if len(self.expenses) == 0:
            print("Нет записей")
            return

        category = input("Введите категорию: ")

        total = 0
        found = False

        for exp in self.expenses:
            if exp.category == category:
                print(f"{exp.amount} руб. | {exp.description}")
                total = total + exp.amount
                found = True

        if found:
            print(f"\nСумма по категории '{category}': {total} руб.")
        else:
            print(f"Расходов в категории '{category}' не найдено")