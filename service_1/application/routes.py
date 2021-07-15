from application import app, db  
from flask import render_template 
import requests


@app.route('/')
def home():
    brand = requests.get('http://watch_api:5000/get_brand')
    material = requests.get('http://watch_api:5000/get_material')
    cost = requests.post('http://watch_api:5000/get_material', data = brand.text + ' '+  material.text)
    return render_template('index.html', brand = brand.text, material = material.text)

 new_cost = price(brand = brand.text, material = material.text, cost = cost.text)
    db.session.add(price)
    db.session.commit()