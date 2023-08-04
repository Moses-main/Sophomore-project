# This is the console based app

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.id] = product

    def update_product(self, id, name, price, quantity):
        if id in self.products:
            self.products[id].name = name
            self.products[id].price = price
            self.products[id].quantity = quantity

    def search_product(self, keyword):
        results = []
        for product in self.products.values():
            if keyword.lower() in product.name.lower():
                results.append(product)
        return results

# Sample usage
inventory = Inventory()

while True:
    print("1. Add Product")
    print("2. Update Product")
    print("3. Search Product")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        inventory.add_product(Product(id, name, price, quantity))
    
    elif choice == '2':
        id = input("Enter product ID to update: ")
        if id in inventory.products:
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            quantity = int(input("Enter new product quantity: "))
            inventory.update_product(id, name, price, quantity)
        else:
            print("Product not found.")
    
    elif choice == '3':
        keyword = input("Enter search keyword: ")
        results = inventory.search_product(keyword)
        for product in results:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    
    elif choice == '4':
        break
      