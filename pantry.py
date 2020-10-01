import psycopg2

class item:
    def __init__(self, name, category, weight, expdate):
        self.conn =  psycopg2.connect(database='pantry',
                                      user='postgres',
                                      password='hahaochiang',
                                      host='34.80.136.214',
                                      port='5432')
        self.cur = self.conn.cursor()
        print("Database connected!")

        self.item = name
        self.category = category
        self.weight = weight
        self.expdate = expdate

        self.cur.execute("INSERT INTO inventory (item, category, weight, expdate) VALUES (%s, %s, %s, %s)",
                        (self.item, self.category, self.weight, self.expdate))
        self.conn.commit()
        print("New item added to your pantry:)")

    def update(self, weight):
        self.cur.execute("UPDATE inventory SET weight=%s", (weight, ))
        self.conn.commit()
        print("updated successfully!")



    