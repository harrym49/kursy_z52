class Product():
    pass

class Car(Product):
    def __init__(self, price, *args):
        self.price = float(price)
        self.args = list(args)

    def description(self):
        print(f"This is a car. It costs {self.price} $. Its parametres are: {self.args[0]} meters in hight,"
              f" {self.args[1]} meters in width and {self.args[2]} in length")

x = Car(24.50, 3,2,7)
x.description()