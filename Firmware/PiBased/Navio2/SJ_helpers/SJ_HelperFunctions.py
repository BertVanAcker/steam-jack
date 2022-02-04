from threading import Thread,Lock,Timer
import re
#steam-jack imports
import sys
if sys.platform.startswith('win'):
    print('Windows environment - imports adapted')
    from Firmware.PiBased.Generic.SJ_helpers import SJ_HelperFunctions
    from Firmware.PiBased.Generic.SJ_helpers import SJ_Constants
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin') or sys.platform.startswith('darwin'):
    print('Linux environment - imports adapted')
    sys.path.append('../')
    from SJ_helpers import SJ_Constants

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

class DeviceCommunicator():

    def __init__(self,DEBUG=False):
           self.DEBUG = DEBUG

    def genericRead(self,data):
        if self.DEBUG:print(data)
        matches = re.findall("(\d{1,3})([A-Z]{1,4})(-?\d{1,18})", data.decode('utf-8'), re.I)
        if matches is None:
            return -1
        else:
            return matches[0][0],matches[0][1],matches[0][2]

    def composeMessage(self,id,cmd,parameter):
        if parameter is not None:
            MESSAGE = (SJ_Constants.SJ_CommandStart + str(id) + cmd + str(parameter) + SJ_Constants.SJ_CommandEnd).encode('utf-8')
        else:
            MESSAGE = (SJ_Constants.SJ_CommandStart + str(id) + cmd + SJ_Constants.SJ_CommandEnd).encode('utf-8')
        return MESSAGE

def mapRange(value, inMin, inMax, outMin, outMax):
    """
          Function to interpret the steam-jack float values
    """
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))