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

# [[expire today], [one day left], [two days left]]
def showWarning():
    data = [[],[],[]]
    zero = today.strftime('%Y-%m-%d')
    one = (today+timedelta(days=1)).strftime('%Y-%m-%d')
    two = (today+timedelta(days=2)).strftime('%Y-%m-%d')
    cur.execute("SELECT item FROM inventory WHERE expdate=%s", (zero, ))
    rows = cur.fetchall()
    for row in rows:
        data[0].append(row) #[(),(),...]
    cur.execute("SELECT item FROM inventory WHERE expdate=%s", (one, ))
    rows = cur.fetchall()
    for row in rows:
        data[1].append(row) #[(),(),...]
    cur.execute("SELECT item FROM inventory WHERE expdate=%s", (two, ))
    rows = cur.fetchall()
    for row in rows:
        data[2].append(row) #[(),(),...]
    return data

def getInventory():
    data = []
    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()
    for row in rows:
        data.append(row) #[(),(),...]
    return data

def getInventoryByDays(days): #date的型別???
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
    return options    