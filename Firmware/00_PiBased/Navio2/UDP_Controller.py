


#generic imports
import socket
import struct
import re
import sys
import time
from threading import Thread,Lock,Timer
import atexit


#device-specific imports
import navio.leds
import navio.util

#----------------------------------constants-------------------------------
#actions
SJ_ActionLED = "LED"
SJ_BlinkLED = "BLK"
SJ_BlinkLEDSTOP = "NBLK"

# LED colors
NAVIO_LED_Black = '0'
NAVIO_LED_Red = '1'
NAVIO_LED_Green = '2'
NAVIO_LED_Blue = '3'
NAVIO_LED_Yellow = '4'
NAVIO_LED_Cyan = '5'
NAVIO_LED_Magenta = '6'
NAVIO_LED_White = '7'

#--------------------------GLOBAL VARIABLES------------------------------
GLOBAL_SOCKET = None
COLOR_ACTIVE = 'Black'
BLINK_STATE = 'OFF'
BLINK_DELAY = 100
GLOBAL_LOCK_LED = Lock()

#---------------------helper class-------------------------------------=
class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()




#-------------------NAVIO2 initialization--------------------------------
led = navio.leds.Led()

def buildinLED(color):
    global led
    with GLOBAL_LOCK_LED:
        print('changing the build-in LED color:'+ color)
        led.setColor(color)

def exit_handler():
    global GLOBAL_SOCKET
    print('Exit function called!')
    GLOBAL_SOCKET.close()

#--------------------threads for async functions-------------------------
def BlinkLED():
    global BLINK_STATE
    if BLINK_STATE == 'OFF':
        buildinLED(COLOR_ACTIVE)
        BLINK_STATE = 'ON'
    elif BLINK_STATE == 'ON':
        buildinLED('Black')
        BLINK_STATE = 'OFF'




#function library
def genericRead(data):
    print(data)
    matches = re.findall("(\d{1,3})([A-Z]{1,4})(-?\d{1,18})", data.decode('utf-8'), re.I)
    if matches is None:
        return -1
    else:
        return matches[0][0],matches[0][1],matches[0][2]

def executeCommand(cmd,parameter):
    global COLOR_ACTIVE
    global BLINK_DELAY
    global BLINK_THREAD

    if cmd == SJ_ActionLED:
        if parameter == NAVIO_LED_Red:
            buildinLED('Red')
            COLOR_ACTIVE = 'Red'
        if parameter == NAVIO_LED_Yellow:
            buildinLED('Yellow')
            COLOR_ACTIVE = 'Yellow'
        if parameter == NAVIO_LED_Green:
            buildinLED('Green')
            COLOR_ACTIVE = 'Green'

    if cmd == SJ_BlinkLED:
        BLINK_DELAY = int(parameter)
        BLINK_THREAD = perpetualTimer(BLINK_DELAY, BlinkLED)  # periodically update sensor!
        BLINK_THREAD.start()

    if cmd == SJ_BlinkLEDSTOP:
        BLINK_THREAD.cancel()




atexit.register(exit_handler)
#-------------------UDP initialization--------------------------------
UDP_IP = '' #socket.gethostname()
UDP_PORT = 6789
#----------------setting up connection and both ports----------------
GLOBAL_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
GLOBAL_SOCKET.bind((UDP_IP,UDP_PORT))
#--------------------------------------------------------------------
print('Navio2 UDP controller initialized')



while(True):
    x=1
    try:
        data, addr = GLOBAL_SOCKET.recvfrom(1024)
        # Parse packet
        id,cmd,value = genericRead(data)

		# execute command
        executeCommand(cmd,value)

        #logging


    except:
        print("ERROR")
