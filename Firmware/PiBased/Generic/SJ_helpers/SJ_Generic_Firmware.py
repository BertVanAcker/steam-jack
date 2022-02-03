
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

    def __init__(self,DEBUG=False):
        self.DEBUG = DEBUG
        self.GLOBAL_SOCKET = None
        #instantiate the steam-jack helpers
        self.deviceHandler = DeviceSpecificFunctions(DEBUG)

        atexit.register(self.exit_handler)


    def start(self):
        # connecting to the UDP socket
        self.connect()
        while True:
            self.update()

    def exit_handler(self):
        print('Exit function called!')
        self.GLOBAL_SOCKET.close()

    def update(self):
        self.nullFunction()

    def connect(self):
        self.nullFunction()

    def executeCommand(self):
        self.nullFunction()


    def nullFunction(self):
        if self.DEBUG:print("Function not implemented on this device")

