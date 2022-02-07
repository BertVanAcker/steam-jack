###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Communicator class handling the generic communication patterns
###################################################################################

#imports
import re
import socket
import serial
from .Communicator_Constants import *

class Communicator():
    """
        Communicator: Class representing the generic communication handler

         :param bool DEBUG: setting the verbose
         :param string UDP_IP: IP address of the target device
         :param string UDP_PORT: UDP port of the target device
         :param string COM_PORT: COM port of the target device
         :param int COM_BAUD: Baud rate of the target device
         :param object Logger: Logger object for uniform logging
    """
    def __init__(self,UDP_IP='192.168.0.110',UDP_PORT=6789,UDP_IP_RESPONSE='192.168.0.150',COM_PORT='COM5',COM_BAUD=SJ_DefaultBaud,DEBUG=True,LOGGER=None):

        #verbose and logging
        self.DEBUG = DEBUG
        self.LOGGER = LOGGER

        #UDP interface
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.UDP_IP_RESPONSE = UDP_IP_RESPONSE
        self.udp_socket_out = None
        self.udp_socket_in = None

        #serial (USB) interface
        self.COM_PORT = COM_PORT
        self.COM_BAUD = COM_BAUD
        self.Serial_socket = None

        #active communcation
        self.activeCOMM = "UDP" #UDP connection [UDP] / UBSserial [Serial]

    def activateSerial(self):
        """
              Function to activate the serial communication method
        """
        self.activeCOMM = "Serial"
        self.Serial_socket = serial.Serial(self.COM_PORT, self.COM_BAUD)
        #close and re-open
        self.Serial_socket.close()
        self.Serial_socket.open()


    def activateUDP(self):
        """
              Function to activate the UDP communication method
        """
        self.activeCOMM = "UDP"
        #activate an outgoing UDP
        self.udp_socket_out = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
        # activate an ingoing UDP
        self.udp_socket_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.udp_socket_in.bind((self.UDP_IP_RESPONSE, SJ_DefaultPortIn))

    def deactivateUDP(self):
        """
              Function to deactivate the UDP communication method
        """
        #de-activate an outgoing UDP
        self.udp_socket_out.close()
        # activate an ingoing UDP
        self.udp_socket_in.close()

    def deactivateSerial(self):
        """
              Function to deactivate the SERIAL communication method
        """
        #de-activate the serial connetion
        self.Serial_socket.close()

    def genericWrite(self,id,cmd,parameter=None):
        """
              Function to compose & write a steam_jack command to the communication bus - Non-blocking

              :param string id: Name identifier of the targetted device
              :param string cmd: Command identifier
              :param list parameters: parameterList

              :return bool writeSuccess: successfull bus write identification (-1 = error)
        """
        #compose the message - independent from active communication
        MESSAGE = self.composeMessage(id,cmd,parameter)

        if self.activeCOMM == "UDP":
            try:
                self.udp_socket_out.sendto(MESSAGE, (self.UDP_IP, self.UDP_PORT))
                self.LOGGER.log(msg="UPD send: "+str(MESSAGE),type="INFO")
            except:
                if self.DEBUG:print("UDP communication failed.")
                self.LOGGER.log(msg="UPD failed: " + str(MESSAGE), type="ERROR")

        elif self.activeCOMM == "Serial":

            self.Serial_socket.write(MESSAGE)
            self.LOGGER.log(msg="Serial send:" + str(MESSAGE), type="INFO")

    def genericWrite_blocking(self,id,cmd,parameter=None):
        """
              Function to compose & write a steam_jack command to the communication bus - blocking

              :param string id: Name identifier of the targetted device
              :param string cmd: Command identifier
              :param list parameters: parameterList

              :return bool writeSuccess: successfull bus write identification (-1 = error)
        """
        #compose the message - independent from active communication
        MESSAGE = self.composeMessage(id,cmd,parameter)

        if self.activeCOMM == "UDP":
            try:
                self.udp_socket_out.sendto(MESSAGE, (self.UDP_IP, self.UDP_PORT))
                self.LOGGER.log(msg="UPD send: "+str(MESSAGE),type="INFO")
            except:
                if self.DEBUG:print("UDP communication failed.")
                self.LOGGER.log(msg="UPD failed: " + str(MESSAGE), type="ERROR")

            #wait for a response on port 5000
            RESPONSE = 0
            while not RESPONSE:
                try:
                    data, addr = self.udp_socket_in.recvfrom(1024)
                    # Parse packet
                    id, cmd, value = self.interpretMessage(data)
                    RESPONSE=1
                    return id, cmd, value
                except:
                    if self.DEBUG:print("ERROR")

        elif self.activeCOMM == "Serial":

            self.Serial_socket.write(MESSAGE)
            self.LOGGER.log(msg="Serial send:" + str(MESSAGE), type="INFO")

            # wait for a response on serial port
            RESPONSE = 0
            while not RESPONSE:
                try:
                    data = self.Serial_socket.readline()
                    print(data)
                    # Parse packet
                    id, cmd, value = self.interpretMessage(data)
                    RESPONSE = 1
                    return id, cmd, value
                except:
                    if self.DEBUG: print("ERROR")

    def interpretMessage(self,data):
        """
              Function to interpret a steam-jack message

              :param string data: steam-jack message

              :return int id: identifier of the message
              :return string cmd: command id of the message
              :return int parameter: parameter of the message
        """
        if self.DEBUG:print(data)
        matches = re.findall("(\d{1,3})([A-Z]{1,4})(-?\d{1,18})", data.decode('utf-8'), re.I)
        if matches is None:
            return -1
        else:
            return matches[0][0],matches[0][1],matches[0][2]

    def composeMessage(self,id,cmd,parameter):
        """
              Function to compose a steam-jack message

              :param int id: identifier of the message
              :param string cmd: command id of the message
              :param int parameter: parameter of the message

              :return string data: steam-jack message
        """
        if parameter is not None:
            MESSAGE = (SJ_CommandStart + str(id) + cmd + str(parameter) + SJ_CommandEnd).encode('utf-8')
        else:
            MESSAGE = ("#" + str(id) + cmd + "\r").encode('utf-8')
        return MESSAGE