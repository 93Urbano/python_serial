import serial, time

#Abrir puerto serie parametrizando
ser = serial.Serial('COM48', 115200, timeout=0, parity=serial.PARITY_NONE, rtscts=1)
print("connected to: " + ser.portstr)

#Enviar el string "3"
ser.write("3\r\n".encode()) #meter encode para codificar el string de texto enviado

# close port
ser.close()             



