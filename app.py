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
    '''elif request.args['action']=="invall":
        item_name = request.form.get('username')
        #exp_date = request.args['expiredate']
        print(item_name, 0)
        item(item_name, 0, 0)'''

@app.route('/get', methods=['GET', 'POST'])
def get():
    print(request.args)
    item_name = request.form.get('username')
    print(item_name)
    print(request.values)
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


