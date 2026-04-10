class InputHandler:


    def get_valid_category(self):
        category = input("Категория: ")
        while category == "":
            print("Ошибка: категория не может быть пустой")
            category = input("Категория: ")
        return category

    def get_valid_amount(self):
        amount = input("Сумма: ")
        while not amount.isdigit():
            print("Ошибка: введите число")
            amount = input("Сумма: ")
        amount = int(amount)
        while amount <= 0:
            print("Ошибка: сумма должна быть больше 0")
            amount = int(input("Сумма: "))
        return amount

    def get_valid_description(self):
        description = input("Описание: ")
        while description == "":
            print("Ошибка: описание не может быть пустым")
            description = input("Описание: ")
        return description

    def get_category_for_filter(self):
        return input("Введите категорию: ")
