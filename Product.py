class Product:
    _id = 0

    def __init__(self, name, price):
        Product._id += 1
        self.id = Product._id
        self.name = name
        self.price = price
