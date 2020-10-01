import psycopg2

class pantry:
    def __init__(self):
        self.conn =  psycopg2.connect(database='pantry',
                                      user='postgres',
                                      password='hahaochiang',
                                      host='34.80.136.214',
                                      port='5432')
        self.cur = self.conn.cursor()
        self.item = ""
        self.weight = 0
        print("Database connected!")

new = pantry()
new.cur.execute("INSERT INTO recipe (item, category, weight) VALUES ('apple', 'fruit', 20)")
new.conn.commit()
    