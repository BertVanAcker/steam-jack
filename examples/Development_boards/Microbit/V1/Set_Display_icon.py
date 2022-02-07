from steam_jack.DeviceLibrary import Microbit_v1
from steam_jack.Communicator.Communicator_Constants import *
import time

#instantiate the device
device = Microbit_v1.Microbit_v1(COM_PORT='COM5',DEBUG=False)


#set the display icon
device.displayIcon(MBT_DISP_HEART)
time.sleep(2)
device.displayIcon(MBT_DISP_CROSS)
time.sleep(2)
device.displayIcon(MBT_DISP_OUT)

device.deactivate()