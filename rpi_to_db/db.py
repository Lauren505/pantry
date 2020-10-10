import psycopg2

conn =  psycopg2.connect(database='pantry',
                                    user='postgres',
                                    password='hahaochiang',
                                    host='34.80.136.214',
                                    port='5432')
cur = conn.cursor()
print("Database connected!")

def getPosition():
    data = []
    cur.execute("SELECT position FROM inventory")
    rows = cur.fetchall()
    for row in rows:
        data.append(row[0])
    return data

def getItem(position):
    cur.execute("SELECT item FROM inventory WHERE position=%s", (position, ))
    data = cur.fetchone()[0]
    return data

def updatePosition(item, position):
    cur.execute("UPDATE inventory SET position = %s WHERE item = %s", (position, item))
    conn.commit()
    print("position updated to db!")

def updateWeight(itemname, weight):
    cur.execute("UPDATE inventory SET weight=%s WHERE item=%s", (weight, itemname))
    conn.commit()
    print("weight updated successfully!")

temp = getPosition()
updatePosition('鮪魚罐頭', [0, 0, 0, 0, 0, 1, 0])
updateWeight('鮪魚罐頭', 600)
print(temp)
print(getItem([0, 0, 0, 0, 0, 1, 0]))