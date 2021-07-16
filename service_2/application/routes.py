from application import app 
from flask import Flask, request 
import random




@app.route('/get_brand', methods=['GET'])
def get_brand():
    return random.choice(['rolex', 'omega', 'vacheron_constantin', 'audemars piguet']) 