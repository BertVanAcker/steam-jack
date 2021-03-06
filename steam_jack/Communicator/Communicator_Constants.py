#####################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Communicator constants corresponding to the communcation protocol
#####################################################################################

# Bus communication
SJ_UDP_IP_IN = '192.168.0.150'
SJ_DefaultBaud = 115200
SJ_DefaultPortIn = 5000

# General
SJ_Timeout = 100        #in ms
SJ_CommandStart = "#"
SJ_CommandEnd = "\r"


#COMMAND constants
SJ_ActionLED = "LED"
SJ_BlinkLED = "BLK"
SJ_BlinkLEDSTOP = "NBLK"
SJ_FetchTemperature = "ATMP"
#response
SJ_Temperature = "RTMP"

# Navio2 constants
NAVIO_LED_Black = '0'
NAVIO_LED_Red = '1'
NAVIO_LED_Green = '2'
NAVIO_LED_Blue = '3'
NAVIO_LED_Yellow = '4'
NAVIO_LED_Cyan = '5'
NAVIO_LED_Magenta = '6'
NAVIO_LED_White = '7'

# Micro:bit constants
MBT_DISP_OUT = '0'
MBT_DISP_HEART = '1'
MBT_DISP_CROSS = '2'



