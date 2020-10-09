from pantry import *
from connection_i2c import *
from flask import Flask, render_template, request, Response
import json
# 缺POSITION
app = Flask(__name__)


'''# continuous update...
if weight!=0:
    # get item from position
    item = ""
    item.update(weight)'''

@app.route('/api', methods=['GET', 'POST'])
def api():
    print(request.args)
    if request.args['action']=="update":
        info = {'temp': current_t, 'humid': current_h, 'warning': showWarning()}
        return Response(json.dumps(info), mimetype='application/json')
    elif request.args['action']=="submit":
        item_name = request.values['item']
        exp_date = request.values['date']
        item(item_name, 0, exp_date)
    elif request.args['action']=="update":
        pass

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route("/add/post_submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        item_name = request.values.get('name')
        exp_date = request.values.get('date')
        item(item_name, 0, exp_date)
    return render_template('add.html')

@app.route('/recipe')
def recipe():
    options = checkrecipe()
    return render_template("recipe.html", options=options)

@app.route('/req_inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        inventory_all = getInventory()
    return render_template("inventory.html", inventory_all=inventory_all)

@app.route('/inventory/by_days', methods=['GET', 'POST'])
def inventorybydays():
    if request.method == 'POST':
        days = request.values.get('days')
        inventory_part = getInventoryByDays(days)
    return render_template("inventory.html", inventory_part=inventory_part)

app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


