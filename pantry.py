import psycopg2
from datetime import datetime, timedelta

today = datetime.today()
conn =  psycopg2.connect(database='pantry',
                                    user='postgres',
                                    password='hahaochiang',
                                    host='34.80.136.214',
                                    port='5432')
cur = conn.cursor()
print("Database connected!")

class item:
    def __init__(self, name, weight, expdate):
        self.item = name
        self.weight = weight
        self.expdate = expdate

        cur.execute("INSERT INTO inventory (item, weight, expdate) VALUES (%s, %s, %s)",
                        (self.item, self.weight, self.expdate))
        cur.execute("INSERT INTO current (name) VALUES (%s) WHERE curritem='curritem'", (self.item, ))
        conn.commit()
        print("New item added to your pantry:)")

    def update(self, weight):
        cur.execute("UPDATE inventory SET weight=%s", (weight, ))
        conn.commit()
        print("updated successfully!")

    def getInfo(self):
        data = []
        cur.execute("SELECT * FROM inventory WHERE item = %s", (self.item, ))
        rows = cur.fetchall()
        for row in rows:
            data.append(row) #[(),(),...]
        return data

def updateWeight(itemname, weight):
    cur.execute("UPDATE inventory SET weight=%s WHERE item=%s", (weight, itemname))
    conn.commit()
    print("updated successfully!")

# [[expire today], [one day left], [two days left]]
def showWarning():
    data = [["expire today: "],["expire tomorrow: "],["expire in two days: "]]
    zero = today.strftime('%Y-%m-%d')
    one = (today+timedelta(days=1)).strftime('%Y-%m-%d')
    two = (today+timedelta(days=2)).strftime('%Y-%m-%d')
    cur.execute("SELECT item FROM inventory WHERE expdate=%s", (zero, ))
    rows = cur.fetchall()
    for row in rows:
        data[0].append(row[0]) #[(),(),...]
    cur.execute("SELECT item FROM inventory WHERE expdate=%s", (one, ))
    rows = cur.fetchall()
    for row in rows:
        data[1].append(row[0]) #[(),(),...]
    cur.execute("SELECT item FROM inventory WHERE expdate=%s", (two, ))
    rows = cur.fetchall()
    for row in rows:
        data[2].append(row[0]) #[(),(),...]
    print(data)
    s = ', '
    print(s.join(data[0]))
    print(type(s.join(data[0])))
    warning = "WARNING!!" + "<br>" + s.join(data[0]) + "<br>" + s.join(data[1]) + "<br>" + s.join(data[2])
    return warning

def getInventory():
    data = []
    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()
    for row in rows:
        data.append(row) #[(),(),...]
    print(data)
    return data

def getInventoryByDays(days): 
    data = []
    date = today+timedelta(days=days)
    date = date.strftime('%Y-%m-%d')
    cur.execute("SELECT * FROM inventory WHERE expdate<=%s", (date, ))
    rows = cur.fetchall()
    for row in rows:
        data.append(row) #[(),(),...]
    return data

# Todo
def checkrecipe():
    recipe=[]
    inventory=[]
    options=[]
    result=[]
    cur.execute("SELECT * FROM recipe")
    rows = cur.fetchall()
    for row in rows:
        recipe.append(row)
    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()
    for row in rows:
        inventory.append([row[0],row[1]])

    for r in recipe:
        count = 0
        dish = r[0]
        for i in range(1,(len(r)//2)):
            for j in range(len(inventory)):
                if r[2*i-1]==inventory[j][0] and r[2*i]==inventory[j][1]:
                    print("here")
                    count+=1
                    break
        if count==((len(r)-2)//2):
            options.append(dish)
    print(options)
    for option in options:
        cur.execute("SELECT * FROM recipe WHERE recipe=%s", (option, ))
        rows = cur.fetchall()
        for row in rows:
            result.append(row)
    print(result)
    return result   

def showrecipe():
    data = []
    cur.execute("SELECT * FROM recipe")
    rows = cur.fetchall()
    for row in rows:
        data.append(row) #[(),(),...]
    print(data)
    return data

def addrecipe(re, n, w):
    cur.execute("INSERT INTO recipe VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (re, n[0], w[0], n[1], w[1], n[2], w[2], n[3], w[3], "https"))
    conn.commit()
    print(re, n[0], w[0], n[1], w[1], n[2], w[2], n[3], w[3], "https")
    print("New recipe added to your cookbook:)")

def getCurItem(pos):
    # according to pos return itemname
    return "吐司"

def getCommon():
    data = []
    cur.execute("SELECT * FROM common")
    rows = cur.fetchall()
    for row in rows:
        data.append(row)
    return data

def setCommon(new):
    cur.execute("INSERT INTO common VALUES (%s)", (new, ))
    conn.commit()