

from tracker import ExpenseTracker


class Menu:
    def __init__(self):
        self.tracker = ExpenseTracker()

    def show_menu(self):
        """Показать меню"""
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать расходы по категории")
        print("4. Выйти")

    def run(self):
        """Запуск программы"""
        while True:
            self.show_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                self.tracker.add_expense()
            elif choice == "2":
                self.tracker.show_all()
            elif choice == "3":
                self.tracker.show_by_category()
            elif choice == "4":
                print("До свидания!")
                break
            else:
                print("Неверный выбор, попробуйте снова")