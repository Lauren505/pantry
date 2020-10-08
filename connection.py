import serial
import serial.tools.list_ports 
import sys
 
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
ser.flushInput()
ser.flushOutput()
 
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {}".format(port, desc))
 
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
