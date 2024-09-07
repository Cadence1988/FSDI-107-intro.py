from flask import Flask, request
import json

app = Flask_name_

@pp.get("/")
def home():
    return "hello from flask"

@pp.get("")




@app.get('/footer')
def footer():
    pageName = {'pageName':'organika'}
    return json.dumps(pageName)
# please vreate an API to footer that contains the name of the page
@pp.get('/api/products')
def products():
    produsts = []
    return json.dumps(products)

@pp.post('/api/produvcts')
def save_products():
    item = request.get_json()
    print (item)/