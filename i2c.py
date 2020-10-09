# key input
# 0: humidity
# 2: tempurature
# 4: weight


from smbus import SMBus

addr = 0x04
bus = SMBus(1)
msg1 = 0
current_h = 0
current_t = 0
weight = 0

while True:
	k = input()
	bus.write_byte(addr,(int)(k))
	msg1 = bus.read_byte(addr)
	bus.write_byte(addr,(int)(k+1))
	msg2 = bus.read_byte(addr)
	print('msg1: {}'.format(msg1))
	print('msg2: {}'.format(msg2))

	if(msg1 or msg2):
		if(k=='0'): 
			current_h = msg1 + 0.01 * msg2
			msg1 = msg2 = 0
		elif(k=='2'):
			current_t = msg1 + 0.01 * msg2
			msg1 = msg2 = 0
		elif(k=='4'):
			weight = msg1 + 0.01 * msg2
			msg1 = msg2 = 0

	print('h: {}'.format(current_h))
	print('t: {}'.format(current_t))
	print('w: {}'.format(weight))




	
