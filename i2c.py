from smbus import SMBus

addr = 0x04
bus = SMBus(1)

while True:
	k = input()
	bus.write_byte(addr,(int)(k))
	print(bus.read_byte(addr))
	
