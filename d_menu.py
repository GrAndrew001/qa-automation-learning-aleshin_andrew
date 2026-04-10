from b_tracker import ExpenseTracker
from c_enter_cost import InputHandler
class Menu:

    def __init__(self):
        self.tracker = ExpenseTracker()
        self.input = InputHandler()

    def show_menu(self):

        print("\n Учёт расходов ")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать расходы по категории")
        print("4. Выйти")

    def add_expense_flow(self):

        print("\nДобавление расхода")

        category = self.input.get_valid_category()
        amount = self.input.get_valid_amount()
        description = self.input.get_valid_description()

        success = self.tracker.add_expense(category, amount, description)

        if success:
            print("Расход добавлен.")
        else:
            print("Не удалось добавить расход.")

    def show_all_flow(self):

        print("\nВсе расходы")

        expenses = self.tracker.get_all_expenses()


        if len(expenses) == 0:
            print("Нет записей")
            return


        i = 1
        for expense in expenses:
            print(f"{i}. {expense.category} | {expense.amount} руб. | {expense.description}")
            i = i + 1


        total = self.tracker.get_total_amount()
        print(f"\nОбщая сумма: {total} руб.")

    def show_by_category_flow(self):

        print("\nРасходы по категории")

        expenses = self.tracker.get_all_expenses()


        if len(expenses) == 0:
            print("Нет записей")
            return


        category = self.input.get_category_for_filter()


        filtered, total = self.tracker.get_expenses_by_category(category)


        if len(filtered) > 0:
            for expense in filtered:
                print(f"{expense.amount} руб. | {expense.description}")
            print(f"\nСумма по категории '{category}': {total} руб.")
        else:
            print(f"Расходов в категории '{category}' не найдено")

    def run(self):
        """Запускает программу"""
        while True:
            self.show_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_expense_flow()
            elif choice == "2":
                self.show_all_flow()
            elif choice == "3":
                self.show_by_category_flow()
            elif choice == "4":
                print("До свидания!")
                break
            else:
                print("Неверный выбор, попробуйте снова")
