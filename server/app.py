from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory catalog (simulated database)
catalog = [
    {"id": 1, "name": "Laptop", "price": 1000, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 500, "category": "Electronics"},
    {"id": 3, "name": "Desk", "price": 300, "category": "Furniture"},
    {"id": 4, "name": "Chair", "price": 150, "category": "Furniture"}
]

# Home endpoint
@app.get("/")
def home():
    return "Welcome to the Product Catalog API"

# GET endpoint to return the entire catalog
@app.get('/api/catalog')
def get_catalog():
    return jsonify(catalog)

# POST endpoint to save a new product
@app.post('/api/catalog')
def save_product():
    new_product = request.get_json()
    catalog.append(new_product)
    return jsonify({"message": "Product added successfully", "product": new_product}), 201

# GET endpoint to calculate and return the total value of the catalog
@app.get('/api/reports/total')
def get_total_value():
    total_value = sum(product["price"] for product in catalog)
    return jsonify({"total_value": total_value})

# GET endpoint to filter products by category
@app.get('/api/products/<category>')
def get_products_by_category(category):
    filtered_products = [product for product in catalog if product["category"].lower() == category.lower()]
    return jsonify(filtered_products)

if __name__ == "__main__":
    app.run(debug=True)
