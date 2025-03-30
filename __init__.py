from flask import Flask
from flask import render_template
from flask import json

                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def index():
    user_value = request.args.get('value')
    if not user_value:
        return "N'oubliez pas saisir un chiffre dans votre URL"
    return f"Valeur saisie : {user_value}"
  
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
