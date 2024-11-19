class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition:
            print(f"Газировка и {self.addition}")
        else:
            print("Обычная газировка")

soda_with_lemon = Soda("Лимон")
soda_with_lemon.show_my_drink()

soda_without_addition = Soda()
soda_without_addition.show_my_drink()