
#generic imports
import socket
from threading import Thread,Lock,Timer
import atexit


#steam-jack imports
import SJ_helpers.SJ_Constants
import SJ_helpers.SJ_DeviceSpecificFunctions
import SJ_helpers.SJ_HelperFunctions

class SJ_Controller():

    def __init__(self,DEBUG=False):
        self.DEBUG = DEBUG
        self.GLOBAL_SOCKET = None
        self.COLOR_ACTIVE = 'Black'
        self.BLINK_STATE = 'OFF'
        self.BLINK_DELAY = 100
        self.BLINK_THREAD = None
        #instantiate the steam-jack helpers
        self.deviceHandler = SJ_helpers.SJ_DeviceSpecificFunctions(DEBUG)
        self.constants = SJ_helpers.SJ_Constants
        self.localCommunicator = SJ_helpers.SJ_HelperFunctions.DeviceCommunicator(DEBUG)

        atexit.register(self.exit_handler)
        #connecting to the UDP socket
        self.connect()


    def exit_handler(self):
        print('Exit function called!')
        self.GLOBAL_SOCKET.close()

    #--------------------threads for async functions-------------------------
    def BlinkLED(self):
        if self.BLINK_STATE == 'OFF':
            self.deviceHandler.buildinLED(self.COLOR_ACTIVE)
            self.BLINK_STATE = 'ON'
        elif self.BLINK_STATE == 'ON':
            self.deviceHandler.buildinLED('Black')
            self.BLINK_STATE = 'OFF'


    def executeCommand(self,cmd,parameter):

        if cmd == self.constants.SJ_ActionLED:
            if parameter == self.constants.NAVIO_LED_Red:
                self.deviceHandler.buildinLED('Red')
                self.COLOR_ACTIVE = 'Red'
            if parameter == self.constants.NAVIO_LED_Yellow:
                self.deviceHandler.buildinLED('Yellow')
                self.COLOR_ACTIVE = 'Yellow'
            if parameter == self.constants.NAVIO_LED_Green:
                self.deviceHandler.buildinLED('Green')
                self.COLOR_ACTIVE = 'Green'

        if cmd == self.constants.SJ_BlinkLED:
            self.BLINK_DELAY = int(parameter)
            self.BLINK_THREAD = SJ_helpers.SJ_HelperFunctions.perpetualTimer(self.BLINK_DELAY, self.BlinkLED)  # periodically update sensor!
            self.BLINK_THREAD.start()

        if cmd == self.constants.SJ_BlinkLEDSTOP:
            self.BLINK_THREAD.cancel()


    def connect(self):
        # -------------------UDP initialization--------------------------------
        UDP_IP = ''  # socket.gethostname()
        UDP_PORT = 6789
        # ----------------setting up connection and both ports----------------
        self.GLOBAL_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.GLOBAL_SOCKET.bind((UDP_IP, UDP_PORT))
        # --------------------------------------------------------------------
        print('Navio2 UDP controller initialized')


    def update(self):
        try:
            data, addr = self.GLOBAL_SOCKET.recvfrom(1024)
            # Parse packet
            id, cmd, value = self.localCommunicator.genericRead(data)
            # execute command
            self.executeCommand(cmd, value)
        except:
            print("ERROR")


controller = SJ_Controller(DEBUG=True)

while True:
    controller.update()
