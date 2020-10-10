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
    if request.args['action']=="refresh":
        info = {'temp': 0, 'humid': 0, 'warning': showWarning(), 'inv': getInventory()} #current_t, current_h, weight
        return Response(json.dumps(info), mimetype='application/json')
    elif request.args['action']=="update": # weight的更新在這裡
        weight = 20 #weight
        itemname = '吐司' #getCurItem(position)
        updateWeight(itemname, weight) #current_t, current_h, weight
        return Response(json.dumps(weight), mimetype='application/json')
    elif request.args['action']=="invall": 
        inventory_all = {'inv': getInventory()}
        print("here")
        return Response(json.dumps(inventory_all), mimetype='application/json')
    elif request.args['action']=="invpart": # undone
        inventory_part = {'inv': getInventory()}
        print("here")
        return Response(json.dumps(inventory_part), mimetype='application/json')
    elif request.args['action']=="showrecipe":
        cookbook = {'cookbook': showrecipe()}
        print("here")
        return Response(json.dumps(cookbook), mimetype='application/json')
    elif request.args['action']=="checkrecipe":
        options = {'options': checkrecipe()}
        print("here")
        return Response(json.dumps(options), mimetype='application/json')

@app.route('/get', methods=['GET', 'POST'])
def get():
    item_name = request.form.get('name')
    exp_date = request.form.get('expdate')
    item(item_name, 0, exp_date)
    print("name: ", item_name, "expdate: ", exp_date)
    return render_template("mainpage.html")

@app.route('/addre', methods=['GET', 'POST'])
def addre():
    re = request.form.get('re')
    n1 = request.form.get('n1')
    w1 = request.form.get('w1')
    n2 = request.form.get('n2')
    w2 = request.form.get('w2')
    n3 = request.form.get('n3')
    w3 = request.form.get('w3')
    n4 = request.form.get('n4')
    w4 = request.form.get('w4')
    n = [n1, n2, n3, n4]
    w = [w1, w2, w3, w4]
    print(n, w)
    addrecipe(re, n, w)
    return render_template("add_recipe.html")

@app.route('/com', methods=['GET', 'POST'])
def com():
    com = request.form.get('com')
    setCommon(com)
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


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


