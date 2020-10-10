from pantry import *
# from connection_i2c import *
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
    if request.args['action']=="update": # weight的更新也要寫在這裡
        info = {'temp': 0, 'humid': 0, 'warning': showWarning(), 'inv': getInventory()} #current_t, current_h, weight
        return Response(json.dumps(info), mimetype='application/json')
    elif request.args['action']=="invall": 
        inventory_all = {'inv': getInventory()}
        print("here")
        return Response(json.dumps(inventory_all), mimetype='application/json')
    elif request.args['action']=="invpart": # undone
        inventory_part = {'inv': getInventory()}
        print("here")
        return Response(json.dumps(inventory_part), mimetype='application/json')
    elif request.args['action']=="recipe":
        options = {'options': checkrecipe()}
        print("here")
        return Response(json.dumps(options), mimetype='application/json')

@app.route('/get', methods=['GET', 'POST'])
def get():
    item_name = request.form.get('name')
    exp_date = request.form.get('expdate')
    item(item_name, 0, exp_date)
    print("name: ", item_name, "expdate: ", exp_date)
    return render_template("add.html")

@app.route('/')
def index():
    return render_template("mainpage.html")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/recipe')
def recipe():
    return render_template("recipe.html")

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    return render_template("inventory.html")

@app.route('/inventory/by_days', methods=['GET', 'POST'])
def inventorybydays():
    if request.method == 'POST':
        days = request.values.get('days')
        inventory_part = getInventoryByDays(days)
    return render_template("inventory.html", inventory_part=inventory_part)

app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


