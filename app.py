from pantry import *

new = item('apple', 'fruit', 20, 20201012)

app = Flask(__name__)

@app.route('/')
def index():
    return 'My Flask App!'


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


