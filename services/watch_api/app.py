from flask import Flask, request 
import random

app = Flask(__name__)

@app.route('/get_brand', methods=['GET'])
def get_brand():
    return random.choice(['rolex', 'omega', 'vacheron_constantin', 'audemars piguet']) 



@app.route('/get_material', methods=['GET'] )
def get_material():
    return random.choice(['18k_Gold', '914L_steel', 'platinum', 'titanium'])

# animal generator route here

# animal noise generator route here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)