#imports
import unittest
import time
from steam_jack.DeviceLibrary import Emlid_navio
from steam_jack.Communicator.Communicator_Constants import *


class test_Communicator(unittest.TestCase):
    def setUp(self):
        self.device = Emlid_navio.Emlid_navio(UDP_IP='192.168.0.110',UDP_PORT=6789,DEBUG=False)
        pass

    def tearDown(self):
        self.device.deactivate()
        time.sleep(1)  # sleep time in seconds


    def test_writeUDP_nonblocking(self):
        self.device.buildinLED(NAVIO_LED_Red)
        time.sleep(2)
        self.device.buildinLED(NAVIO_LED_Green)
        time.sleep(2)
        self.device.buildinLED(NAVIO_LED_Yellow)