from threading import Thread,Lock,Timer
import socket
import sys

#device-specific imports
if sys.platform.startswith('win'):
    print('Windows environment - imports adapted')
    from Firmware.PiBased.Generic.SJ_helpers.SJ_Constants import *
    from Firmware.PiBased.Generic.SJ_helpers.SJ_HelperFunctions import *
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin')or sys.platform.startswith('darwin'):
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

    #-------------------------------------------------------------------------------------
    #
    #      Device specifics
    #
    #-------------------------------------------------------------------------------------
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

    def ActionLED_function(self,parameter=None):
        if parameter == NAVIO_LED_Red:
            self.buildinLED('Red')
            self.COLOR_ACTIVE = 'Red'
        if parameter == NAVIO_LED_Yellow:
            self.buildinLED('Yellow')
            self.COLOR_ACTIVE = 'Yellow'
        if parameter == NAVIO_LED_Green:
            self.buildinLED('Green')
            self.COLOR_ACTIVE = 'Green'

    def BlinkLED_function(self,parameter=None):
        self.BLINK_DELAY = int(parameter)
        self.BLINK_THREAD = perpetualTimer(self.BLINK_DELAY, self.BlinkLED)  # periodically update sensor!
        self.BLINK_THREAD.start()

    def BlinkLEDSTOP_function(self,parameter=None):
        self.BLINK_THREAD.cancel()

    def FetchTemperature_function(self,parameter=None):
        #dummy temperature -40<->50
        temperature = 22.5
        temperature_scaled = mapRange(value=temperature,inMin=-40, inMax=50, outMin=0, outMax=1000)
        return temperature_scaled




