from pantry import *
from flask import Flask, render_template

app = Flask(__name__)

data = []
pumpkin = item('pumpkin', 'fruit', 200, 20201012)
data = pumpkin.getInfo()

@app.route('/')
def index():
    return render_template("index.html")
    '''for item in data:
        for detail in item:
            return detail'''


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


