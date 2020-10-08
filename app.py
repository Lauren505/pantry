from pantry import *
from flask import Flask, render_template

app = Flask(__name__)

data = []
pumpkin = item('pumpkin', 'fruit', 200, 20201012)
data = pumpkin.getInfo()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/recipe')
def recipe():
    return render_template("recipe.html")

@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


