from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Home endpoint
@app.get("/")
def home():
    return "hello from flask"

# About endpoint
@app.get("/about")
def about():
    me = {'name': 'Ryan Marlow'}
    return jsonify(me)

# Footer API endpoint
@app.get('/footer')
def footer():
    pageName = {'pageName': 'organika'}
    return jsonify(pageName)

@app.get('/api/products')
def products():
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 1000},
        {'id': 2, 'name': 'Smartphone', 'price': 500},
        {'id': 3, 'name': 'Tablet', 'price': 300}
    ]
    return jsonify(products)

# API to save a new product
@app.post('/api/products')
def save_products():
    item = request.get_json()
    print(item)  
    
    return jsonify({"message": "Product saved successfully", "product": item}), 201

if __name__ == "__main__":
    app.run(debug=True)
