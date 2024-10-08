from flask import Flask, request
import json
from config import db
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # warning, this disables CORS policy

@app.get("/")
def home():
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name":"adrian Aguinaga"}
    return json.dumps(me)

@app.get("/footer")#i know that this is a section not a page
def footer():
    pageName = {"pageName":"organika"}
    return json.dumps(pageName)
# please create an API to footer that contains the name of the page (organika)

products = []

def fix_id(obj):
    obj["_id"]= str(obj["_id"])
    return obj

@app.get("/api/products")
def read_products():
    cursor = db.catalog.find({})
    catalog = []
    for prod in cursor:
        catalog.append(fix_id(prod))

    return json.dumps(catalog)    



@app.post("/api/products")
def save_products():
    item = request.get_json()    
    db.catalog.insert_one(item)
    return json.dumps(fix_id(item))

@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    if 0<=index<len(products):
        products[index]=update_item
        return json.dumps(update_item)
    else:
        return "That index does not exist"
    

# post /api/coupons -> save a coupon
@app.get("/api/coupons")
def get_coupons():
    cursor = db.coupons.find({})
    coupons = []
    for cp in cursor:
        coupons.append(fix_id(cp))
    return json.dumps(coupons)  
  
# post /api/coupons -> save a coupon
@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    return json.dumps({"message": "Coupon added successfully", "coupon": coupon}), 201

@app.get("/api/coupons/search/<string:code>")
def search_coupon_by_code(code):
    coupon = db.coupons.find_one({"code": code})
    if coupon:
        return json.dumps(fix_id(coupon))
    return json.dumps({"error": "Coupon not found"}), 404


# GET endpoint to return the entire catalog
@app.get("/api/catalog")
def get_catalog():
    cursor = db.catalog.find({})
    catalog = [fix_id(prod) for prod in cursor]
    return json.dumps(catalog)

# POST endpoint to save a new product
@app.post("/api/catalog")
def save_product():
    new_product = request.get_json()
    db.catalog.insert_one(new_product)
    return json.dumps({"message": "Product added successfully", "product": new_product}), 201

# GET endpoint to filter products by category
@app.get("/api/catalog/<category>")
def get_products_by_category(category):
    cursor = db.catalog.find({"category": category})
    filtered_products = [prod for prod in cursor]
    return json.dumps(filtered_products)



app.run(debug=True)   
"""

@app.post("/api/coupons")
def save_coupon() 
"""
# coupon struct:
# code - str
# discount - number

"""
{
"code: "qwerty",
"discount": 12
}
"""









#from flask import Flask, request, jsonify
#import json

#app = Flask(__name__)

# Home endpoint
#@app.get("/")
#def home():
 #   return "hello from flask"

# About endpoint
#@app.get("/about")
#def about():
 #   me = {'name': 'Ryan Marlow'}
  #  return jsonify(me)

# Footer API endpoint
#@app.get('/footer')
#def footer():
 #   pageName = {'pageName': 'organika'}
  #  return jsonify(pageName)

#@app.get('/api/products')
#def products():
 #   products = [
  #      {'id': 1, 'name': 'Laptop', 'price': 1000},
   #     {'id': 2, 'name': 'Smartphone', 'price': 500},
    #    {'id': 3, 'name': 'Tablet', 'price': 300}
    #]
    #return jsonify(products)

# API to save a new product
#@app.post('/api/products')
#def save_products():
 #   item = request.get_json()
  #  print(item)  
    
   # return jsonify({"message": "Product saved successfully", "product": item}), 201

#if __name__ == "__main__":
 #   app.run(debug=True)
