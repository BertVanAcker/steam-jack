import json

class Notebook():
    """
        Notebook: Class representing the jupyter notebook template

         :param string Name: Name of the DomainVariable
         :param string Description: Description of the DomainVariable
         :param objectList content: ObjectList with the content for the notebook
    """

    def __init__(self, JSONDescriptor=None, Name="", Description="",content = [], DEBUG=True):
        self.DEBUG = DEBUG
        if JSONDescriptor is None:
            self.Name = Name
            self.Description = Description
            self.Content = content

        else:
            self.json2object(JSONDescriptor)
            x = 10

    def json2object(self, jsonDescriptor):
        """
             Function to generate a Notebook object from a JSON file

             :param string jsonDescriptor: absolute path to the json file for the DomainVariable

        """

        # --interpret JSON file--
        with open(jsonDescriptor, "r") as read_file:
            jsonObject = json.load(read_file)


    def object2json(self):
        """
               Function to generate a json file from the notebook model
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

class Cell():  #
    """
        Cell: Class representing the jupyter notebook cell template

         :param string Title: Title for the notebook cell
         :param string Text: Text for the notebook cell
         param string Code: Code for the notebook cell
         :param string CellType: CellType of the notebook cell (markdown|code|raw)
    """

    def __init__(self, JSONDescriptor=None, Title="", Text="", Code="", Type='markdown', DEBUG=True):
        self.DEBUG = DEBUG
        if JSONDescriptor is None:
            self.Title = Title
            self.Text = Text
            self.Code = Code
            self.Type = Type

        else:
            self.json2object(JSONDescriptor)
            x = 10

    def json2object(self, jsonDescriptor):
        """
             Function to generate a Notebook cell object from a JSON file

             :param string jsonDescriptor: absolute path to the json file for the DomainVariable

        """

        # --interpret JSON file--
        with open(jsonDescriptor, "r") as read_file:
            jsonObject = json.load(read_file)

    def object2json(self):
        """
               Function to generate a json file from the Notebook cell
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class FirmwarePrototype():  #
    """
        FirmwarePrototype: Class representing the device firmware prototype

         :param string Name: Name for the device firmware
         :param string Description: Description for the device firmware
         :param string DeviceName: Name of the device for the device firmware
         :param ObjectList FunctionPrototypes: ObjectList with the function prototypes for the firmware
    """

    def __init__(self, JSONDescriptor=None, Name="", Description="", DeviceName="",functionPrototypes = [], DEBUG=True):
        self.DEBUG = DEBUG
        if JSONDescriptor is None:
            self.Name = Name
            self.Description = Description
            self.DeviceName = DeviceName
            self.FunctionPrototypes = functionPrototypes

        else:
            self.json2object(JSONDescriptor)
            x = 10

    def json2object(self, jsonDescriptor):
        """
             Function to generate a firmwarePrototype object from a JSON file

             :param string jsonDescriptor: absolute path to the json file for the firmwarePrototype

        """

        # --interpret JSON file--
        with open(jsonDescriptor, "r") as read_file:
            jsonObject = json.load(read_file)

    def object2json(self):
        """
               Function to generate a json file from the firmwarePrototype
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class FunctionPrototype():  #
    """
        FunctionPrototype: Class representing a device firmware function prototype

         :param string PartName: Partname of the function prototype
         :param string Description: Description for the function prototype
         :param list parameters: parameterList of the function prototype
         :param list ReturnValues: Return values of the function prototype
    """

    def __init__(self, JSONDescriptor=None, partName="", Description="", parameterList=[],returnList = [], DEBUG=True):
        self.DEBUG = DEBUG
        if JSONDescriptor is None:
            self.partName = partName
            self.Description = Description
            self.ParameterList = parameterList
            self.ReturnList = returnList

        else:
            self.json2object(JSONDescriptor)
            x = 10

    def json2object(self, jsonDescriptor):
        """
             Function to generate a firmwarePrototype object from a JSON file

             :param string jsonDescriptor: absolute path to the json file for the firmwarePrototype

        """

        # --interpret JSON file--
        with open(jsonDescriptor, "r") as read_file:
            jsonObject = json.load(read_file)

    def object2json(self):
        """
               Function to generate a json file from the firmwarePrototype
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class FunctionParameter():  #
    """
        FunctionParameter: Class representing a function parameter

         :param string Name: Parameter Name
         :param string Description: Description for the parameter
         :param string Datatype: Datatype of the parameter
         :param string Default: Default value for the parameter
    """

    def __init__(self, JSONDescriptor=None, Name="", Description="", default="",datatype='enum',enumDefinition=[], DEBUG=True):
        self.DEBUG = DEBUG
        if JSONDescriptor is None:
            self.Name = Name
            self.Description = Description
            self.Default = default
            self.Datatype = datatype
            self.EnumDefinition = enumDefinition