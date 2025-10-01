class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def calculate_price(self) -> float:
        return self.price


class Drink(MenuItem):
    def __init__(self, name, price, size: str):
        super().__init__(name, price)
        self.size = size
    
    def calculate_price(self) -> float:
        if self.size == "Pequeña":
            return self.price
        elif self.size == "Mediana":
            return self.price + 5.0
        elif self.size == "Grande":
            return self.price + 10.0
        else:
            raise ValueError("Tamaño inválido")


class Appetizer(MenuItem):
    def __init__(self, name, price, portions: int):
        super().__init__(name, price)
        self.portions = portions
    
    def calculate_price(self) -> float:
        return self.price * self.portions
        

class MainCourse(MenuItem):
    def __init__(self, name, price, extra: int):
        super().__init__(name, price)
        self.extra = extra
    
    def calculate_price(self) -> float:
        if self.extra == 0:
            return self.price
        else:
            return self.price + (8.0 * self.extra)


class Dessert(MenuItem):
    def __init__(self, name, price, portions: int):
        super().__init__(name, price)
        self.portions = portions
    
    def calculate_price(self) -> float:
        return self.price * self.portions


class Order:
    def __init__(self):
        self.items = []
    
    def add_items(self, item: MenuItem):
        self.items.append(item)
    
    def total_price(self) -> float:
        return sum(item.calculate_price() for item in self.items)

    def show_order(self):
        print("---- FACTURA ----")
        for item in self.items:
            print(f"{item.name}: $ {item.calculate_price():.2f}")
        print("-----------------")
        print(f"Total: $ {self.total_price():.2f}")
        print("-----------------")


# Menú con 12 ítems
menu = [
    Drink("Coca-Cola", 5.0, "Grande"),
    Drink("Agua", 3.0, "Pequeña"),
    Drink("Jugo", 4.0, "Mediana"),
    Appetizer("Papas fritas", 8.0, 2),
    Appetizer("Aros de Cebolla", 10.0, 1),
    Appetizer("Alitas BBQ", 12.0, 2),
    MainCourse("Hamburguesa", 15.0, 1),
    MainCourse("Pasta Pesto", 12.0, 0),
    MainCourse("Pizza", 20.0, 2),
    Dessert("Helado", 6.0, 2),
    Dessert("Brownie", 7.0, 1),
    Dessert("Pudín", 5.0, 1)
]

# Pedido de ejemplo
pedido = Order()
pedido.add_items(menu[0])
pedido.add_items(menu[3])
pedido.add_items(menu[5])
pedido.add_items(menu[3])

pedido.show_order()


