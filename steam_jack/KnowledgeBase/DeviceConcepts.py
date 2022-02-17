###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Device concepts
###################################################################################

class Device():
    """
        Device: Class representing a device

         :param string Name: Name of the Device
         :param string Description: Description of the Device
         :param string Version: Version of the Device
         :param enum Type: Type of the Device (Robot|MeasurementDevice|EmbeddedPlatform)
         :param objectlist SupportedFunctions: List of supported functions
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,Name="",Description="",Version="0.0.1",Type='Robot',SupportedFunctions=[]  ,DEBUG=True):

        #verbose and logging
        self.DEBUG = DEBUG
        self.Name = Name
        self.Description = Description
        self.Type = Type
        self.Version = Version
        self.SupportedFunctions = SupportedFunctions

    def addFunction(self,functionName):
        """
             Function to add a supported function by name and search a abstract definition

             :param string functionName: exact name of the function

        """
        #todo:implement


class SupportedFunction():
    """
        SupportedFunction: class representing the device supported function

         :param object AbstractFunction: Reference to the abstract function
         :param string Version: Version of the Device
         :param object FunctionImplementation: Implementation description of the supported function

    """
    def __init__(self, AbstractFunction=None, FunctionImplementation=None, Version="0.0.1", DEBUG=True):

        self.DEBUG = DEBUG
        self.AbstractFunction = AbstractFunction
        self.FunctionImplementation = FunctionImplementation
        self.Version = Version



class FunctionImplementation():
    """
        FunctionImplementation: class representing the function implementation of a device

         :param bool isImplemented: Identify if the function is implemented or not
         :param enum Formalism: The used formalism (micropython|python|javascript|arduinoC|blockcode)
         :param string LibraryCode: structured code for Libraries
         :param string DeclarationCode: structured code for declarations
         :param string CodeSection: structured code
         :param string loopCode: structured code for the loop
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,isImplemented=False,Formalism="arduinoC",LibraryCode="",DeclarationCode="",CodeSection="",loopCode="",DEBUG=True):

        #verbose and logging
        self.DEBUG = DEBUG
        self.isImplemented = isImplemented
        self.Formalism = Formalism
        self.LibraryCode = LibraryCode
        self.DeclarationCode = DeclarationCode
        self.CodeSection = CodeSection
        self.loopCode = loopCode

