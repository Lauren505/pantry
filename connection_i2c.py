# key input
# 0,1: humidity
# 2,3: temperature
# 4: sign of weight_diff (-:1,+:2)
# 5,6: weight
# 7: closing door

import time
from smbus import SMBus 
import db

addr = 0x04
bus = SMBus(1)
msg = [0,0,0,0,0,0,0]
current_h = 0
current_t = 0
takePic = 0

time.sleep(5)	

while True:
	for i in range(0,7):
		bus.write_byte(addr, i)
		msg[i] = bus.read_byte(addr)
		time.sleep(0.5)		
	print('msg: {}'.format(msg))
	current_h = msg[0] + 0.01 * msg[1]
	current_t = msg[2] + 0.01 * msg[3]
	weight_diff = msg[5] + 0.01 * msg[6]
	if(weight_diff!=0):
		takePic = 1
		print("----take picture----")
	if msg[4]==1:
		weight_diff *=-1
	'''
	if msg[4]!=0:
		msg[5] = bus.read_byte(addr)
		time.sleep(3)
		msg[6] = bus.read_byte(addr)
		time.sleep(3)
		weight_diff = msg[5] + 0.01 * msg[6]
		if msg[4]==1:
			weight_diff *=-1
	'''
	
	print('h: {}'.format(current_h))
	print('t: {}'.format(current_t))
	print('w: {}'.format(weight_diff))

	if(takePic==1):
		obj = getItem(getPosition)
		previous_weight = obj.weight
		updateWeight(obj, previous_weight+weight_diff)
		takePic = 0







	
