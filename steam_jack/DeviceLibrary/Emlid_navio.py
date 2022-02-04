###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Device class representing the emlid navio 2
#
#   Note:           Emlid firmware under Firmware/PiBased/Navio2
###################################################################################
#imports
import time

from steam_jack.Communicator import Communicator,Communicator_Constants
from steam_jack.Logger import Logger

class Emlid_navio():
    """
        Emlid_navio: Class representing emlid navio 2 device, interfaced via UDP

         :param bool DEBUG: setting the verbose
         :param string UDP_IP: IP address of the target device
         :param int UDP_PORT: UDP port of the target device
    """
    def __init__(self,UDP_IP='192.168.0.110',UDP_PORT=6789,DEBUG=False):
        self.logger = Logger.Logger(fileName="logs/Emlid-navio.log")
        self.communicator = Communicator.Communicator(UDP_IP=UDP_IP, UDP_PORT=UDP_PORT, LOGGER=self.logger,DEBUG=DEBUG)

        #activating the UDP communication method
        self.communicator.activateUDP()

    def deactivate(self):
        """
              Function deactivate the device
        """
        self.communicator.deactivateUDP()

    def buildinLED(self, color):
        """
              Function to set the color of the buildin LED - Non-blocking

              :param string color: predefined color - see communcation protocol
        """
        self.communicator.genericWrite(id=1, cmd=Communicator_Constants.SJ_ActionLED,parameter=color)


    def blinkLED(self,delay):
        """
              Function to blink the build-in LED with the active color - non-blocking

              :param int delay: delay in ms
        """
        self.communicator.genericWrite(id=1, cmd=Communicator_Constants.SJ_BlinkLED,parameter=delay)

    def stopBlinkLED(self):
        """
              Function to stop blinking the buildin LED with the active color - non-blocking

        """
        self.communicator.genericWrite(id=1, cmd=Communicator_Constants.SJ_BlinkLEDSTOP,parameter=0)

    def getTemperature(self):
        """
              Function to fetch the temperature - blocking

              :return float temperature: temperature value (-40 <-> +50)

        """
        ID,CMD,temperature = self.communicator.genericWrite_blocking(id=1, cmd=Communicator_Constants.SJ_FetchTemperature,parameter=0)
        temperature_scaled = self.mapRange(value=int(temperature),inMin=0, inMax=1000, outMin=-40, outMax=50)
        return temperature_scaled

    def mapRange(self,value, inMin, inMax, outMin, outMax):
        """
              Function to interpret the steam-jack float values

        """
        return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))