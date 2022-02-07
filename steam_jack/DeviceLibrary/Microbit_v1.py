###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Device class representing the BBC Micro:bit v1
#
#   Note:           Micro:bit v1 firmware under Firmware/CBased/MicroBit_v1
#                   or
#                   Makeblock code: Serial-Interpreter-test (PoC)
###################################################################################
#imports
import time

from steam_jack.Communicator import Communicator,Communicator_Constants
from steam_jack.Logger import Logger

class Microbit_v1():
    """
        Microbit v1: Class representing the BBC micro:bit v1, interfaced via serial (USB)

         :param bool DEBUG: setting the verbose
         :param int COM_PORT: COM port of the target device
    """
    def __init__(self,COM_PORT='COM5',DEBUG=False):
        self.logger = Logger.Logger(fileName="logs/Microbit.log")
        self.communicator = Communicator.Communicator(COM_PORT, LOGGER=self.logger,DEBUG=DEBUG)

        #activating the UDP communication method
        self.communicator.activateSerial()

    def deactivate(self):
        """
              Function deactivate the device
        """
        self.communicator.deactivateSerial()


    def displayIcon(self, icon):
        """
              Function to visualize an icon on the microbit display - Non-blocking

              :param string icon: predefined icons - see communcation protocol
        """
        self.communicator.genericWrite(id=1, cmd=Communicator_Constants.SJ_ActionLED,parameter=icon)


