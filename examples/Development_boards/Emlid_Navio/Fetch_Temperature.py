#imports
import time
from steam_jack.DeviceLibrary import Emlid_navio
from steam_jack.Communicator.Communicator_Constants import *

#instantiate the device
device = Emlid_navio.Emlid_navio(UDP_IP='192.168.0.110',UDP_PORT=6789,DEBUG=False)

#change the color of the build-in LED
device.buildinLED(NAVIO_LED_Green)

#fetch the temperature
temperature = device.getTemperature()
print(temperature)

device.deactivate()