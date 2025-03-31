from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1, valeur + 1):  # On boucle de 1 à 'valeur' (le nombre de lignes)
        espaces = ' ' * (valeur - j)  # On calcule le nombre d'espaces avant les étoiles pour centrer
        etoiles += espaces + '*' * j + '<br>'  # Ajouter les étoiles et un saut de ligne
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
