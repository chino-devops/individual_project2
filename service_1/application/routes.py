from application import app, db  
from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy 
import requests

class costs(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement = True)
    brand = db.Column(db.String(30), nullable=False)
    material = db.Column(db.String(40), nullable=False)
    cost = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    brand = requests.get('http://service_2:5000/get_brand')
    material = requests.get('http://service_3:5000/get_material')
    cost = requests.post('http://service_4:5000/get_cost', data = brand.text + ' '+  material.text)

    all_costs = costs.query.all()

    new_cost = costs(brand = brand.text, material = material.text, cost = cost.text)
    db.session.add(str(new_cost))
    db.session.commit()


    return render_template('index.html', brand = brand.text, material = material.text, cost = cost.text)

 