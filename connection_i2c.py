# key input
# 0,1: humidity
# 2,3: temperature
# 4: sign of weight_diff (-:1,+:2)
# 5,6: weight
# 7: closing door

from time import sleep
from smbus import SMBus

addr = 0x04
bus = SMBus(1)
msg = [0,0,0,0,0,0]
current_h = 0
current_t = 0
weight = 0

while True:
	for i in range(0,5):
		bus.write_byte(addr, i)
		msg[i] = bus.read_byte(addr)
		time.sleep(3)
	print('msg: {}'.format(msg))
	current_h = msg[0] + 0.01 * msg[1]
	current_t = msg[2] + 0.01 * msg[3]
	weight = msg[5] + 0.01 * msg[6]
	
	print('h: {}'.format(current_h))
	print('t: {}'.format(current_t))
	print('w: {}'.format(weight))








	
