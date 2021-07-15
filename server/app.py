from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    brand = requests.get('http://watch_api:5000/get_brand')
    material = requests.get('http://watch_api:5000/get_material')
    cost = requests.post('http://watch_api:5000/get_material', data = brand.text + ' '+  material.text)
    return render_template('index.html', brand = brand.text, material = material.text)

# home route here
# must query the animal API for an animal and a noise – the noise should be based on the animal

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)