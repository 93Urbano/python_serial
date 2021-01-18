import serial, time

#Abrir puerto serie parametrizando
ser = serial.Serial('COM48', 115200, timeout=0, parity=serial.PARITY_NONE, rtscts=1) 
print("connected to: " + ser.portstr)

#Bucle principal
while True:
    if(ser.in_waiting > 0): #imprimir 
        line = ser.readline() #leer lineas con salto de carro
        print(line)




