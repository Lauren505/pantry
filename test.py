'''recipe=[["番茄炒蛋","番茄",200,"雞蛋",100,"洋蔥",100,"蒜頭",50,"url"],["番茄濃湯","番茄",200,"馬鈴薯",50,"蒜頭",20,"洋蔥",50,"url"]]
inventory=[["番茄",200],["雞蛋",100],["洋蔥",100],["蒜頭",50]]
options=[]

for r in recipe:
    count = 0
    dish = r[0]
    for i in range(1,(len(r)//2)):
        for j in range(len(inventory)):
            if r[2*i-1]==inventory[j][0] and r[2*i]==inventory[j][1]:
                count+=1
                break
    if count==((len(r)-2)//2):
        options.append(dish)

print(options)'''

'''from pantry import *
test = item("a","b",1,1)
test.checkrecipe()'''

from datetime import datetime, timedelta
today = datetime.today()
dif = 8
# date = (today+timedelta(days=dif))
date = (today+timedelta(days=dif)).strftime('%Y-%m-%d')
print(date)
print(today.strftime('%Y-%m-%d'))
if "2020-10-15"<date:
    print("yes")