###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	STEAM language concepts
###################################################################################
from steam_jack.Documentor.DocumentorObjects import *


class STEAMLanguage():
    """
        STEAMLanguage: Class representing the complete STEAMLanguage

         :param string Name: Name of the Device
         :param string Description: Description of the Device
         :param string Version: Version of the Device
         :param objectlist LanguageConcepts: List of generic language concepts
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,Name="",Description="",Version="0.0.1",LanguageConcepts=[]  ,DEBUG=True):
        self.DEBUG = DEBUG
        self.Name = Name
        self.Description = Description
        self.Version = Version
        self.LanguageConcepts = LanguageConcepts

class LanguageConcept():
    """
            LanguageConcept: Class representing a STEAM LanguageConcept, containing different languageElements

             :param string Name: Name of the LanguageElement
             :param string Description: Description of the LanguageElement
             :param enum Domain: Domain of the LanguageElement (Robotics|Electronics|RocketEngineering|SmartFarming)
             :param objectList LanguageElements: List of corresponding LanguageElements
             :param bool DEBUG: setting the verbose

        """
    def __init__(self,Name="",Description="",Domain="Robotics",LanguageElements=[]  ,DEBUG=True):

        #verbose and logging
        self.DEBUG = DEBUG
        self.Name = Name
        self.Description = Description
        self.Domain = Domain
        self.LanguageElements = LanguageElements


class LanguageElement():
    """
        LanguageElement: Class representing a STEAM LanguageElement, possibly with multiple user interfaces

         :param string Name: Name of the LanguageElement
         :param string Description: Description of the LanguageElement
         :param objectList AbstractFunctions: List of corresponding abstract functions
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,Name="",Description="",AbstractFunctions=[]  ,DEBUG=True):

        #verbose and logging
        self.DEBUG = DEBUG
        self.Name = Name
        self.Description = Description
        self.AbstractFunctions = AbstractFunctions

    def documentation(self):
        docs=[]
        heading = Header(Text=self.Name, Level=1)
        description = Paragraph(Text=self.Description)
        docs.append(GenericDocument(Name=self.Name, content=[heading, description]))
        for func in self.AbstractFunctions:
            for subdoc in func.documentation():
                docs.append(subdoc)

        return docs




class AbstractFunction():
    """
        AbstractFunction: class representing the abstract function, coupled to the languageElement

         :param string Name: Name of the Device
         :param string Description: Description of the Device
         :param enum Complexity: Complexity level (entry|intermediate|advanced|...)
         :param enum FunctionType: Type of the function (COMMAND|EVENT|STRING|NUMBER|BOOLEAN|CONDITIONAL)
         :param enum FunctionClass: Class of the function (PERCEPTION|LOGIC|ACTION)
         :param object UserInterface: User interface of the abstract function

    """
    def __init__(self, Name="",Description="", Complexity="entry",FunctionType="COMMAND",UserInterface=None, DEBUG=True):

        self.DEBUG = DEBUG
        self.Name=Name
        self.Description=Description
        self.FunctionType = FunctionType
        self.UserInterface=UserInterface
        self.Complexity = Complexity

    def documentation(self):
        docs = []
        heading = Header(Text=self.Name, Level=2)
        if self.Complexity=="entry":level = "Beginner"
        if self.Complexity=="intermediate":level = "Normaal"
        if self.Complexity=="advanced":level = "Geadvanceerd"
        complexity = Paragraph(Text="Gebruikersinterface moeilijkheidsgraad: "+ level)
        description = Paragraph(Text=self.Description)

        docs.append(GenericDocument(Name=self.Name, content=[heading,complexity, description]))
        for subdoc in self.UserInterface.documentation():
            docs.append(subdoc)

        return docs

class UserInterface():
    """
        FunctionImplementation: class representing the function implementation of a device

         :param bool isImplemented: Identify if the function is implemented or not
         :param enum Formalism: The used formalism (micropython|python|javascript|arduinoC|blockcode)
         :param string FunctionPartName: partname of the function
         :param string BlockIcon: Reference to the block icon/image
         :param string ExtensionID: unique ID of the extension
         :param string ExtensionCategory: unique name of the extension category
         :param object UI_Example: User interface example
         :param objectList FunctionParameters: Object list of the function parameters
         :param objectList FunctionReturns: Object list of the function parameters
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,isImplemented=False,Formalism="arduinoC",FunctionPartName="",BlockIcon="",ExtensionID="",ExtensionCategory="",UI_Examples=[],FunctionParameters=[],FunctionReturns=[],DEBUG=True):

        #verbose and logging
        self.DEBUG = DEBUG
        self.isImplemented = isImplemented
        self.Formalism = Formalism
        #cde-based UI
        self.FunctionPartName = FunctionPartName
        #block-based UI
        self.BlockIcon=BlockIcon
        self.ExtensionID=ExtensionID
        self.ExtensionCategory=ExtensionCategory
        #UI example depending on formalism
        if self.Formalism=="blockcode":
            self.UI_Examples_BlockCode=UI_Examples
            self.UI_Examples_Code=[]
        else:
            self.UI_Examples_Code = UI_Examples
            self.UI_Examples_BlockCode = []

        self.FunctionParameters=FunctionParameters
        self.FunctionReturns = FunctionReturns

    def getExample(self):
        if len(self.UI_Examples_Code) is not 0:
            return self.UI_Examples_Code
        if len(self.UI_Examples_BlockCode) is not 0:
            return self.UI_Examples_BlockCode

    def documentation(self):
        docs = []
        content = []
        #provide the code template or block
        if self.Formalism == "blockcode":
            UI_content = Image(ImagePath=self.BlockIcon)
        else:
            functionPrototype = ""

            parameterList = ""
            for parameter in self.FunctionParameters:
                if parameter == self.FunctionParameters[-1]:
                    parameterList = parameterList+parameter.Name
                else:
                    parameterList = parameterList + parameter.Name + ','
            returnList = ""
            for parameter in self.FunctionReturns:
                if parameter == self.FunctionReturns[-1]:
                    returnList = returnList + parameter.Name
                else:
                    returnList = returnList + parameter.Name + ','

            if self.Formalism=='python':
                functionPrototype = returnList+' = '+self.FunctionPartName+"("+parameterList+")"
            #TODO:add other formalisms
            UI_content = CodeSection(Formalism=self.Formalism,Code=functionPrototype)

        content.append(UI_content)

        #describe the function parameters
        if len(self.FunctionParameters) is not 0:
            content.append(Header(Text="Functie parameters",Level=3))
            content.append(Paragraph(Text="De volgende parameters worden gebruikt in de functie:"))
            parameterDescription=[]
            for parameter in self.FunctionParameters:
                parameterDescription.append(parameter.documentation())
            content.append(ListSection(Bullet="-",ListElements=parameterDescription))

        # describe the function returns
        return_content = []
        if len(self.FunctionReturns) is not 0:
            content.append(Header(Text="Functie returns", Level=3))
            content.append(Paragraph(Text="De functie geeft volgende parameters terug:"))
            parameterDescription = []
            for parameter in self.FunctionReturns:
                parameterDescription.append(parameter.documentation())
            content.append(ListSection(Bullet="-", ListElements=parameterDescription))


        docs.append(GenericDocument(Name="UI description", content=content))

        #fetch example documents
        for example in self.UI_Examples_Code:
            docs.append(example.documentation())
        for example in self.UI_Examples_BlockCode:
            docs.append(example.documentation())


        return docs


class CodeExample():
    """
        CodeExample: class representing the code-based example

         :param string Title: Title of the example
         :param string Description: Description of the example
         :param enum Formalism: The used formalism (micropython|python|javascript|arduinoC)
         :param string Code: structured code
         :param bool DEBUG: setting the verbose

    """

    def __init__(self,Title="",Description="",Formalism="python", Code="", DEBUG=True):
        # verbose and logging
        self.DEBUG = DEBUG
        self.Title = Title
        self.Description=Description
        self.Formalism = Formalism
        self.Code = Code

    def documentation(self):
        #document content
        heading = Header(Text=self.Title,Level=2)
        description = Paragraph(Text=self.Description)
        code = CodeSection(Code=self.Code,Formalism=self.Formalism)
        return GenericDocument(Name="Example - Code",content=[heading,description,code])

class BlockExample():
    """
        BlockExample: class representing the block-based example

         :param string Title: Title of the example
         :param string Description: Description of the example
         :param enum Formalism: The used formalism (blockcode)
         :param string ExampleBlockCodeReference: reference to the example image
         :param bool DEBUG: setting the verbose

    """

    def __init__(self,Title="",Description="",Formalism="blockcode", BlockCodeReference="", DEBUG=True):
        # verbose and logging
        self.DEBUG = DEBUG
        self.Title = Title
        self.Description=Description
        self.Formalism = Formalism
        self.BlockCodeReference = BlockCodeReference        #image of the example

    def documentation(self):
        #document content
        heading = Header(Text=self.Title,Level=2)
        description = Paragraph(Text=self.Description)
        image = Image(ImagePath=self.BlockCodeReference)
        return GenericDocument(Name="Example - Code",content=[heading,description,image])


class functionParameter():
    """
        functionParameter: Class representing the functionParameter

         :param string Name: Name of the parameter
         :param string Description: Description of the parameter
         :param enum Datatype: Datatype of the Device (integer|boolean|float|...)
         :param objectlist LanguageConcepts: List of generic language concepts
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,Name="",Description="",Datatype="integer" ,DEBUG=True):
        self.DEBUG = DEBUG
        self.Name = Name
        self.Description = Description
        self.Datatype = Datatype

    def documentation(self):
        return self.Datatype+" "+self.Name+": "+ self.Description