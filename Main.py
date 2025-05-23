import abc
import time
import random

class CafeSimulator:
    def __init__(self):
        self.menu = CafeMenu()
        self._initialize_menu()
        self.total_revenue = 0.0

    def _initialize_menu(self):
        # Початкові позиції меню
        self.menu.add_item(Beverage("Кава", 2.50, 10, 200, True))
        self.menu.add_item(Beverage("Чай", 2.00, 8, 250, True))
        self.menu.add_item(Beverage("Сік Апельсиновий", 3.00, 5, 300, False))
        self.menu.add_item(FoodItem("Сендвіч з куркою", 5.50, 60, 250, False))
        self.menu.add_item(FoodItem("Овочевий салат", 4.80, 45, 300, True))
        self.menu.add_item(FoodItem("Десерт Брауні", 3.20, 20, 150, False))
        print("Кафе 'Затишок' відкрито! Меню готове.")

    def display_main_menu(self):
        print("\n--- Головне Меню Кафе ---")
        print("1. Показати меню")
        print("2. Прийняти замовлення")
        print("3. Управління меню (додати/видалити)")
        print("4. Переглянути дохід")
        print("5. Вийти")

    def show_cafe_menu(self):
        print("\n--- Меню Кафе 'Затишок' ---")
        print(self.menu)  # Використання __str__ CafeMenu
        input("\nНатисніть Enter, щоб продовжити...")

    def take_order(self):
        print("\n--- Прийняття Замовлення ---")
        if not self.menu:
            print("Меню порожнє! Додайте позиції.")
            return

        current_order_items = []
        total_order_price = 0.0
        total_preparation_time = 0

        while True:
            self.show_cafe_menu()  # Повторно показуємо меню
            item_name = input("Введіть назву позиції для замовлення (або 'готово' для завершення): ").strip()

            if item_name.lower() == 'готово':
                break

            found_item = self.menu.find_item_by_name(item_name)
            if found_item:
                current_order_items.append(found_item)
                total_order_price += found_item.price
                total_preparation_time += found_item.preparation_time
                print(f"Додано: {found_item.name}. Поточна сума: {total_order_price:.2f} грн.")
            else:
                print(f"Позиції '{item_name}' немає в меню.")

        if not current_order_items:
            print("Замовлення порожнє.")
            return

        print("\n--- Ваше Замовлення ---")
        for item in current_order_items:
            print(f"- {item.name}")
        print(f"Загальна сума до сплати: {total_order_price:.2f} грн.")
        print(f"Приблизний час приготування: {total_preparation_time} секунд.")

        confirm = input("Підтвердити замовлення? (так/ні): ").lower()
        if confirm == 'так':
            print("Готуємо ваше замовлення...")
            time.sleep(total_preparation_time / 5)  # Імітуємо швидке приготування
            print("Замовлення готове! Приємного апетиту!")
            self.total_revenue += total_order_price
        else:
            print("Замовлення скасовано.")

        input("\nНатисніть Enter, щоб продовжити...")

    def manage_cafe_menu(self):
        while True:
            print("\n--- Управління Меню Кафе ---")
            print("1. Додати нову позицію")
            print("2. Видалити позицію")
            print("3. Відсортувати меню за ціною")
            print("4. Фільтрувати: лише напої")
            print("5. Фільтрувати: лише страви")
            print("6. Назад до головного меню")

            choice = input("Оберіть дію: ")

            if choice == '1':
                item_type = input("Тип позиції (напій/страва): ").lower()
                name = input("Назва: ")
                try:
                    price = float(input("Ціна: "))
                    prep_time = int(input("Час приготування (секунди): "))
                    if item_type == "напій":
                        volume = int(input("Об'єм (мл): "))
                        is_hot = input("Гарячий? (так/ні): ").lower() == 'так'
                        self.menu.add_item(Beverage(name, price, prep_time, volume, is_hot))
                    elif item_type == "страва":
                        weight = int(input("Вага (грами): "))
                        is_veg = input("Вегетаріанська? (так/ні): ").lower() == 'так'
                        self.menu.add_item(FoodItem(name, price, prep_time, weight, is_veg))
                    else:
                        print("Невідомий тип позиції.")
                except ValueError:
                    print("Некоректний ввід для ціни/часу/об'єму/ваги.")
            elif choice == '2':
                name_to_remove = input("Введіть назву позиції для видалення: ")
                self.menu.remove_item(name_to_remove)
            elif choice == '3':
                sorted_items = self.menu.sort_by_price()
                print("\n--- Меню відсортовано за ціною ---")
                for item in sorted_items:
                    print(item)
            elif choice == '4':
                beverages = self.menu.filter_by_type("напій")
                print("\n--- Напої ---")
                for item in beverages:
                    print(item)
            elif choice == '5':
                food_items = self.menu.filter_by_type("страва")
                print("\n--- Страви ---")
                for item in food_items:
                    print(item)
            elif choice == '6':
                break
            else:
                print("Некоректний вибір, спробуйте ще раз.")
            input("\nНатисніть Enter, щоб продовжити...")

    def view_revenue(self):
        print(f"\nЗагальний дохід кафе: {self.total_revenue:.2f} грн.")
        input("\nНатисніть Enter, щоб продовжити...")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Оберіть дію: ")
            if choice == '1':
                self.show_cafe_menu()
            elif choice == '2':
                self.take_order()
            elif choice == '3':
                self.manage_cafe_menu()
            elif choice == '4':
                self.view_revenue()
            elif choice == '5':
                break
            else:
                print("Некоректний вибір. Спробуйте ще раз.")


# Запуск гри
if __name__ == "__main__":
    # Класи MenuItem, Beverage, FoodItem, CafeMenu повинні бути тут вище
    # ... (код класів з попередньої відповіді) ...
    # Ось приклад для цих класів, що треба вставити на початку main.py
    class MenuItem(abc.ABC):
        def __init__(self, name: str, price: float, preparation_time: int):
            self._name = name
            self._price = price
            self._preparation_time = preparation_time

        @property
        def name(self) -> str:
            return self._name

        @property
        def price(self) -> float:
            return self._price

        @property
        def preparation_time(self) -> int:
            return self._preparation_time

        @abc.abstractmethod
        def get_description(self) -> str:
            pass

        def __str__(self) -> str:
            return f"{self.name} ({self.price:.2f} грн) - {self.preparation_time} с"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, prep_time={self.preparation_time})"


    class Beverage(MenuItem):
        def __init__(self, name: str, price: float, preparation_time: int, volume_ml: int, is_hot: bool):
            super().__init__(name, price, preparation_time)
            self._volume_ml = volume_ml
            self._is_hot = is_hot

        @property
        def volume_ml(self) -> int:
            return self._volume_ml

        @property
        def is_hot(self) -> bool:
            return self._is_hot

        def get_description(self) -> str:
            temp = "Гарячий" if self._is_hot else "Холодний"
            return f"{self.name} ({self.volume_ml} мл, {temp})"

        def __str__(self) -> str:
            return f"{self.get_description()} - {self.price:.2f} грн"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, prep_time={self.preparation_time}, volume_ml={self.volume_ml}, is_hot={self.is_hot})"


    class FoodItem(MenuItem):
        def __init__(self, name: str, price: float, preparation_time: int, weight_grams: int, is_vegetarian: bool):
            super().__init__(name, price, preparation_time)
            self._weight_grams = weight_grams
            self._is_vegetarian = is_vegetarian

        @property
        def weight_grams(self) -> int:
            return self._weight_grams

        @property
        def is_vegetarian(self) -> bool:
            return self._is_vegetarian

        def get_description(self) -> str:
            veg_status = "Вегетаріанська" if self._is_vegetarian else "Невегетеріанська"
            return f"{self.name} ({self.weight_grams} г, {veg_status})"

        def __str__(self) -> str:
            return f"{self.get_description()} - {self.price:.2f} грн"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, prep_time={self.preparation_time}, weight_grams={self.weight_grams}, is_vegetarian={self.is_vegetarian})"


    class CafeMenu:
        def __init__(self):
            self._items = []

        def add_item(self, item: MenuItem):
            if not isinstance(item, MenuItem):
                raise TypeError("Можна додавати лише об'єкти типу MenuItem або його підкласів.")
            self._items.append(item)
            print(f"'{item.name}' додано до меню.")

        def remove_item(self, name: str) -> bool:
            initial_len = len(self._items)
            self._items = [item for item in self._items if item.name.lower() != name.lower()]
            if len(self._items) < initial_len:
                print(f"'{name}' видалено з меню.")
                return True
            print(f"Позиція '{name}' не знайдена в меню.")
            return False

        def find_item_by_name(self, name: str) -> MenuItem | None:
            return next((item for item in self._items if item.name.lower() == name.lower()), None)

        def filter_by_type(self, item_type: str) -> list[MenuItem]:
            if item_type.lower() == "напій":
                return [item for item in self._items if isinstance(item, Beverage)]
            elif item_type.lower() == "страва":
                return [item for item in self._items if isinstance(item, FoodItem)]
            return []

        def sort_by_price(self, reverse: bool = False) -> list[MenuItem]:
            return sorted(self._items, key=lambda item: item.price, reverse=reverse)

        def sort_by_preparation_time(self, reverse: bool = False) -> list[MenuItem]:
            return sorted(self._items, key=lambda item: item.preparation_time, reverse=reverse)

        def __str__(self) -> str:
            if not self._items:
                return "Меню порожнє."
            menu_str = ""
            for item in self._items:
                menu_str += f"- {item}\n"
            return menu_str.strip()  # Прибираємо зайвий перенос рядка в кінці

        def __repr__(self) -> str:
            return f"CafeMenu(items={repr(self._items)})"

        def __len__(self):
            return len(self._items)


    game = CafeSimulator()
    game.run()