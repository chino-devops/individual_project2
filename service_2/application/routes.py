from flask import Flask, requests 
import random




@app.route('/get_brand', methods=['GET'])
def get_brand():
    return random.choice(['rolex', 'omega', 'vacheron_constantin', 'audemars piguet']) 