from threading import Thread,Lock,Timer
import re

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