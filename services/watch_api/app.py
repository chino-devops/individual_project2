from flask import Flask, request 
import random

app = Flask(__name__)

@app.route('/get_brand', methods=['GET'])
def get_brand():
    return random.choice(['rolex', 'omega', 'vacheron_constantin', 'audemars piguet']) 



@app.route('/get_material', methods=['GET'] )
def get_material():
    return random.choice(['18k_gold', '914L_steel', 'platinum', 'titanium'])

@app.route('/gen_cost', methods=['post'] )
def gen_cost():
    data = request.data.decode('utf-8')
    data = data.split(' ')
    brand = data[0]
    material = data[1]
    
    if brand == 'rolex':
        if material == '18k_gold':
            return '£39,000'
        elif material == '914L_steel':
            return '£5,900'
        elif material == 'platinum':
            return '£31,590'
        elif material == 'titanium':
            return '£25,900'
    elif brand == 'omega':
        if material == '18k_gold':
            return '£25,900'
        elif material == '914L_steel':
            return '£3,900'
        elif material == 'platinum':
            return '£21,590'
        elif material == 'titanium':
            return '£18,900'
    elif brand == 'vacheron_constatin':
        if material == '18k_gold':
            return '£39,590'
        elif material == '914L_steel':
            return '£19,900'
        elif material == 'platinum':
            return '£28,590'
        elif material == 'titanium':
            return '£21,900'
    elif brand == 'audemars_piguet':
        if material == '18k_gold':
            return '£49,590'
        elif material == '914L_steel':
            return '£5,900'
        elif material == 'platinum':
            return '£31,590'
        elif material == 'titanium':
            return '£25,900'
    else:
        return "please enter a correct choice" 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)