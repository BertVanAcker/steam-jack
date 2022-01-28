import socket

UDP_IP = socket.gethostname()        #for testing purpose
#UDP_IP = "192.168.0.110"        #NAVIO
UDP_PORT = 6789  #9090

id=1
cmd = "L"
color = 1
MESSAGE = ("#" + str(id) + cmd +str(color)+ "\r").encode('utf-8')
print(MESSAGE)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE.__str__())

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))