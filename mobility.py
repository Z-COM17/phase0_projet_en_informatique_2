from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    """
    retourne le contenu de la page index.html
    """
    return render_template('index.html')

@app.route('/page.html')
def page():
    """
    retourne le contenu de la page page.html
    """
    return  render_template('page.html')