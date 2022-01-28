#generic imports
import socket
import struct
import re
import sys
import time

#device-specific imports
import navio.leds
import navio.util

#----------------------------------constants-------------------------------
#actions
NAVIO_ActionLED = "LED"

# LED colors
NAVIO_LED_Black = 0
NAVIO_LED_Red = 1
NAVIO_LED_Green = 2
NAVIO_LED_Blue = 3
NAVIO_LED_Yellow = 4
NAVIO_LED_Cyan = 5
NAVIO_LED_Magenta = 6
NAVIO_LED_White = 7

#-------------------NAVIO2 initialization--------------------------------
led = navio.leds.Led()




#function library
def genericRead(data):

    matches = re.findall("(\d{1,3})([A-Z]{1,4})(-?\d{1,18})", data.decode('utf-8'), re.I)
    if matches is None:
        return -1
    else:
        return matches[0][0],matches[0][1],matches[0][2]

def executeCommand(cmd,parameter):
    print(cmd+str(parameter))
    if cmd == NAVIO_ActionLED:
        if parameter == NAVIO_LED_Red:
            led.setColor('Red')






#-------------------UDP initialization--------------------------------
UDP_IP = socket.gethostname()
UDP_PORT = 6789
#----------------setting up connection and both ports----------------
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP,UDP_PORT))
#--------------------------------------------------------------------
print('Navio2 UDP controller initialized')



while(True):
    x=1
    try:
        data, addr = sock.recvfrom(1024)
        # Parse packet
        id,cmd,value = genericRead(data)

		# execute command
        executeCommand(cmd,value)

        #logging


    except:
        print("ERROR")
