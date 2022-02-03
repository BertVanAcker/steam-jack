#imports
import unittest
import time
from steam_jack.Logger import Logger
from steam_jack.Communicator import Communicator, Communicator_Constants


class test_Communicator(unittest.TestCase):
    def setUp(self):
        self.logger = Logger.Logger(fileName="logs/steamjack.log")
        self.communicator = Communicator.Communicator(UDP_IP='192.168.0.110',UDP_PORT=6789,LOGGER=self.logger)

        pass

    def tearDown(self):
        self.communicator.deactivateUDP()
        time.sleep(1)  # sleep time in seconds


    def test_writeUDP_nonblocking(self):
        self.communicator.activateUDP()
        self.communicator.genericWrite(id=1,cmd=Communicator_Constants.SJ_ActionLED,parameter=Communicator_Constants.NAVIO_LED_Red)
        time.sleep(5)
        self.communicator.genericWrite(id=1, cmd=Communicator_Constants.SJ_ActionLED,parameter=Communicator_Constants.NAVIO_LED_Yellow)