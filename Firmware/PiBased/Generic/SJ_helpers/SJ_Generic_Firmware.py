
#generic imports
import socket
import atexit

#steam-jack imports
import sys
if sys.platform.startswith('win'):
    print('Windows environment - imports adapted')
    from Firmware.PiBased.Generic.SJ_helpers import SJ_Constants
    from Firmware.PiBased.Generic.SJ_helpers import SJ_HelperFunctions
    from Firmware.PiBased.Generic.DeviceSpecific.DeviceSpecific import DeviceSpecificFunctions
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin') or sys.platform.startswith('darwin'):
    print('Linux environment - imports adapted')
    sys.path.append('../')
    from SJ_helpers import SJ_Constants
    from SJ_helpers import SJ_HelperFunctions
    from DeviceSpecific.DeviceSpecific import DeviceSpecificFunctions





class SJ_Controller():

    def __init__(self,UDP_IP='',UDP_PORT=6789,DEBUG=False):
        self.DEBUG = DEBUG

        #UDP config
        self.GLOBAL_SOCKET = None
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT

        #instantiate the steam-jack helpers
        self.localCommunicator = SJ_HelperFunctions.DeviceCommunicator(DEBUG)
        atexit.register(self.exit_handler)


    def start(self):
        # connecting to the UDP socket
        self.connect()
        while True:
            self.update()

    def exit_handler(self):
        print('Exit function called!')
        self.GLOBAL_SOCKET.close()


    def connect(self):
        # ----------------setting up connection and both ports----------------
        self.GLOBAL_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.GLOBAL_SOCKET.bind((self.UDP_IP, self.UDP_PORT))
        # --------------------------------------------------------------------
        print('Firmware communication initialized')


    def update(self):
        try:
            data, addr = self.GLOBAL_SOCKET.recvfrom(1024)
            # Parse packet
            id, cmd, value = self.localCommunicator.genericRead(data)
            # execute command
            self.executeCommand(cmd, value)
        except:
            print("ERROR")

    def executeCommand(self, cmd, parameter):

        if cmd == SJ_Constants.SJ_ActionLED:
            self.SJ_ActionLED_function(parameter)
        if cmd == SJ_Constants.SJ_BlinkLED:
            self.SJ_BlinkLED_function(parameter)
        if cmd == SJ_Constants.SJ_BlinkLEDSTOP:
            self.SJ_BlinkLEDSTOP_function(parameter)

    def nullFunction(self):
        if self.DEBUG:print("Function not implemented on this device")

    def SJ_ActionLED_function(self):
        self.nullFunction()

    def SJ_BlinkLED_function(self):
        self.nullFunction()

    def SJ_BlinkLEDSTOP_function(self):
        self.nullFunction()

