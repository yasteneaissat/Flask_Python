from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def pyramide(valeur):
    resultat = '<pre>'
    
    for i in range(1, valeur + 1):
        # Créer la partie avant le sommet
        gauche = ''.join(str(x) for x in range(1, i + 1))
        # Créer la partie après le sommet
        droite = ''.join(str(x) for x in range(i - 1, 0, -1))
        
        # Ajouter les espaces nécessaires pour centrer
        espaces = ' ' * (valeur - i)
        
        # Combiner tout cela
        resultat += espaces + gauche + droite + '\n'
    
    resultat += '</pre>'
    return resultat

 
if __name__ == "__main__":
    app.run(debug=True)
