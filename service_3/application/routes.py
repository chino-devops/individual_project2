from application import app 
from flask import Flask, request
import random



@app.route('/get_material', methods=['GET'] )
def get_material():
    return random.choice(['18k_gold', '914L_steel', 'platinum', 'titanium'])
