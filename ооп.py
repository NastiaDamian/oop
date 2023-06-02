#a
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print("Shop name:", self.shop_name)
        print("Store type:", self.store_type)

    def open_shop(self):
        print("The online shop is now open!")


store = Shop("MyShop", "Electronics")
print("Shop name:", store.shop_name)
print("Store type:", store.store_type)

store.describe_shop()
store.open_shop()

#b

class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print("Shop name:", self.shop_name)
        print("Store type:", self.store_type)


store1 = Shop("Shop1", "Type1")
store2 = Shop("Shop2", "Type2")
store3 = Shop("Shop3", "Type3")

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

#c

class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print("Shop name:", self.shop_name)
        print("Store type:", self.store_type)
        print("Number of units:", self.number_of_units)


store = Shop("Shop", "Apple")
print("Initial number of units:", store.number_of_units)

store.number_of_units = 10
print("Updated number of units:", store.number_of_units)

store.describe_shop()

#d
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print("Shop name:", self.shop_name)
        print("Store type:", self.store_type)
        print("Number of units:", self.number_of_units)

    def set_number_of_units(self, new_units):
        self.number_of_units = new_units

    def increment_number_of_units(self, increment):
        self.number_of_units += increment


store = Shop("Shop", "Apple")
print("Initial number of units:", store.number_of_units)

store.set_number_of_units(10)
print("Updated number of units:", store.number_of_units)

store.increment_number_of_units(5)
print("Incremented number of units:", store.number_of_units)

store.describe_shop()

#e
class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discount_products(self):
        print("Discounted products:", self.discount_products)


store_discount = Discount("Discount", "Apple")
store_discount.discount_products = ["Product1", "Product2", "Product3"]

store_discount.get_discount_products()



