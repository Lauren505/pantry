import serial, sys
 
ser = serial.Serial('/dev/ttyS0', 9600, timeout=5)
ser.flushInput()
ser.flushOutput()
 
 
if not ser.isOpen():
    ser.open()
    print("Start receive...")
 
 
try:
    while True:
        if not ser.isOpen():
            ser.open()
        # if ser.in_waiting:
        data_raw = ser.readline()
        print(data_raw.decode())
        data = sys.stdin.readline()
        ser.write(str.encode(data))
except KeyboardInterrupt:
    ser.close()
    print('bye')