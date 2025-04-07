from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def fibonacci(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])  # Ajouter le terme suivant de la suite de Fibonacci
    return f"<h1>Suite de Fibonacci jusqu'au {n}-ième terme :</h1><p>{', '.join(map(str, fib[:n]))}</p>"

if __name__ == "__main__":
    app.run(debug=True)
