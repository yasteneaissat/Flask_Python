from flask import Flask
from flask import render_template
from flask import json

                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/<int:valeur>')
def exercice():
    return valeur






                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
