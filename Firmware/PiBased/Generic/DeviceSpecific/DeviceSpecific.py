from threading import Thread,Lock,Timer
import socket
import sys
#device-specific imports
if sys.platform.startswith('win'):
    print('Windows environment - imports adapted')
    from Firmware.PiBased.Generic.SJ_helpers.SJ_Constants import *
    from Firmware.PiBased.Generic.SJ_helpers.SJ_HelperFunctions import *
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    print('Linux environment - imports adapted')
    sys.path.append('../')
    from SJ_helpers.SJ_Constants import *
    from SJ_helpers.SJ_HelperFunctions import *



class DeviceSpecificFunctions():

    def __init__(self,DEBUG=False):
        self.DEBUG = DEBUG
        #threadsafe locking mechanism for device drivers
        self.GLOBAL_LOCK_LED = Lock()
        self.GLOBAL_SOCKET = None
        self.COLOR_ACTIVE = 'Black'
        self.BLINK_STATE = 'OFF'
        self.BLINK_DELAY = 100
        self.BLINK_THREAD = None

    # -------------------General command functions--------------------------
    def executeCommand(self, cmd, parameter):

        if cmd == SJ_ActionLED:
            if parameter == NAVIO_LED_Red:
                self.buildinLED('Red')
                self.COLOR_ACTIVE = 'Red'
            if parameter == NAVIO_LED_Yellow:
                self.buildinLED('Yellow')
                self.COLOR_ACTIVE = 'Yellow'
            if parameter == NAVIO_LED_Green:
                self.buildinLED('Green')
                self.COLOR_ACTIVE = 'Green'

        if cmd == SJ_BlinkLED:
            self.BLINK_DELAY = int(parameter)
            self.BLINK_THREAD = perpetualTimer(self.BLINK_DELAY,self.BlinkLED)  # periodically update sensor!
            self.BLINK_THREAD.start()
        if cmd == SJ_BlinkLEDSTOP:
            self.BLINK_THREAD.cancel()



    #thread-safe LED function
    def buildinLED(self,color):
        with self.GLOBAL_LOCK_LED:
            if self.DEBUG:print('changing the build-in LED color:'+ color)

    #thread-safe LED BLINK function
    def BlinkLED(self):
        if self.BLINK_STATE == 'OFF':
            self.buildinLED(self.COLOR_ACTIVE)
            self.BLINK_STATE = 'ON'
        elif self.BLINK_STATE == 'ON':
            self.buildinLED('Black')
            self.BLINK_STATE = 'OFF'

    def connect(self):
        # -------------------UDP initialization--------------------------------
        UDP_IP = ''  # socket.gethostname()
        UDP_PORT = 6789
        # ----------------setting up connection and both ports----------------
        self.GLOBAL_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.GLOBAL_SOCKET.bind((UDP_IP, UDP_PORT))
        # --------------------------------------------------------------------
        print('Navio2 emulator initialized')

        return self.GLOBAL_SOCKET