"""
Problém: Veľký „if-else“ blok v Order triede
Riešenie: Použiť Factory Pattern, aby sme mohli dynamicky vytvárať rôzne typy objednávok.
"""


class Order:
    def __init__(self, order_type: str):
        self.type = order_type

    def process(self):
        if self.type == "standard":
            print("Processing standard order...")
        elif self.type == "express":
            print("Processing express order...")
        else:
            print("Unknown order type!")

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Notification:
    def notify(self, message: str):
        print(f"Notification: {message}")


if __name__ == "__main__":
    order = Order("standard")
    print(f"Processing order: {order.type}")
    order.process()
    