from threading import Thread,Lock,Timer
#device-specific imports
import navio.leds
import navio.util


class SJ_DeviceSpecificFunctions():

    def __init__(self,DEBUG=False):
        self.DEBUG = DEBUG
        #threadsafe locking mechanism for device drivers
        self.GLOBAL_LOCK_LED = Lock()

        #device instances
        self.led = navio.leds.Led()

    #thread-safe LED function
    def buildinLED(self,color):
        with self.GLOBAL_LOCK_LED:
            if self.DEBUG:print('changing the build-in LED color:'+ color)
            self.led.setColor(color)