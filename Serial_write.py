import serial, time

ser = serial.Serial('COM48', 115200, timeout=0, parity=serial.PARITY_NONE, rtscts=1)  # open serial port
print("connected to: " + ser.portstr)

ser.write("3\r\n".encode())
print(b'0x31')

ser.close()             # close port



