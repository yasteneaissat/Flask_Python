from flask import Flask

app = Flask(__name__)

# Fonction pour générer la suite de Fibonacci jusqu'à n
def fibonacci(n):
    fib = [0, 1]  # Initialiser la suite avec les deux premiers termes
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])  # Ajouter un terme en suivant la relation Un = Un-1 + Un-2
    return fib

@app.route('/<int:n>')
def afficher_fibonacci(n):
    # Si n est 1, on renvoie juste [0]
    if n == 1:
        fib_sequence = [0]
    else:
        # Générer la suite de Fibonacci jusqu'à n termes
        fib_sequence = fibonacci(n)
    
    # Convertir la suite en chaîne pour l'affichage
    result = ', '.join(map(str, fib_sequence))
    
    # Retourner le résultat formaté
    return f"<h1>Suite de Fibonacci jusqu'au {n}-ième terme :</h1><p>{result}</p>"

if __name__ == "__main__":
    app.run(debug=True)
