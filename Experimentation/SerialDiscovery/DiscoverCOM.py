import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for port in ports:
    print(port.description)


Serial_socket = serial.Serial(port.name, 115200)

#send to test
MESSAGE = ("#1LED2\r").encode('utf-8')
Serial_socket.write(MESSAGE)

