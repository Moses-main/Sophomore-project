from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, id, name, price, quantity):
        for product in self.products:
            if product.id == id:
                product.name = name
                product.price = price
                product.quantity = quantity
                break

    def search_product(self, keyword):
        results = []
        for product in self.products:
            if keyword.lower() in product.name.lower():
                results.append(product)
        return results

inventory = Inventory()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_product():
    id = request.form["id"]
    name = request.form["name"]
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])
    product = Product(id, name, price, quantity)
    inventory.add_product(product)
    return redirect(url_for("index"))

@app.route("/update", methods=["POST"])
def update_product():
    id = request.form["id"]
    name = request.form["name"]
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])
    inventory.update_product(id, name, price, quantity)
    return redirect(url_for("index"))

@app.route("/search", methods=["POST"])
def search_product():
    keyword = request.form["keyword"]
    results = inventory.search_product(keyword)
    return render_template("search_results.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
      