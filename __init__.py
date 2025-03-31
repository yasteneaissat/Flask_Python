from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1, valeur + 1): 
        espaces = ' ' * (valeur - j) 
        etoiles += espaces + '*' * j + '<br>' 
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
