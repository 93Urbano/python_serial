import serial, time

ser = serial.Serial('COM48', 115200, timeout=0, parity=serial.PARITY_NONE, rtscts=1)  # open serial port
print("connected to: " + ser.portstr)

while True:
    line = ser.readline()
    if(ser.in_waiting > 0):
        print(line)




