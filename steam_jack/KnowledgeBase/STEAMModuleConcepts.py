###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	STEAM module concepts
###################################################################################
from steam_jack.Documentor.DocumentorObjects import *
from steam_jack.Documentor.CustomMarkdownParser import CustomMarkdownParser


class STEAMModule():
    """
        STEAMModule: Class representing a single STEAM module

         :param string Name: Name of the Device
         :param string Description: Description of the Device
         :param string Version: Version of the Device
         :param objectlist ModuleContent: List of content elements
         :param list requiredFunctions: List of required functions (by name)
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,Title="",Description="",Version="0.0.1",Content=[],requiredFunctions=[],DEBUG=True):
        self.DEBUG = DEBUG
        self.Title = Title
        self.Description = Description
        self.Version = Version
        self.Content = Content
        self.requiredFunctions=requiredFunctions

        self.customRenderer = CustomMarkdownParser()

    def documentation(self):
        docs=[]
        content = []
        #add introduction
        for element in self.Content:
            if element.isIntroduction:
                for subdoc in element.documentation():
                    docs.append(subdoc)
        #add required functions
        content.append(Header(Text="Nodige functies", Level=3))
        content.append(Paragraph(Text="De volgende STEAM functies zijn nodig tijdens deze STEAM module:"))
        reqFunctions = []

        for funcName in self.requiredFunctions:
            #TODO:fetch function by name + format the module reference
            f = funcName
            reqFunctions.append("Link naar "+f)

        content.append(ListSection(Bullet="-", ListElements=reqFunctions))
        docs.append(GenericDocument(Name=self.Title, content=content))

        #TODO:add supported devices (resolve using functions)

        #add content
        for element in self.Content:
            if not element.isIntroduction:
                for subdoc in element.documentation():
                    docs.append(subdoc)

        return docs

class ModuleContent():
    """
        ModuleContent: Class representing a module content

         :param string Name: Name of the LanguageElement
         :param string Description: Description of the LanguageElement
         :param string ContentFileReference: Reference to the Markdown content file
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,Name="",ContentFileReference="" ,isIntroduction=False ,DEBUG=True):

        #verbose and logging
        self.DEBUG = DEBUG
        self.Name = Name
        self.isIntroduction = isIntroduction
        self.customRenderer = CustomMarkdownParser()
        self.ContentFile = self.customRenderer.render_markdown2GenericDocument(document=ContentFileReference)


    def documentation(self):
        docs=[]
        heading = Header(Text=self.Name, Level=1)
        docs.append(GenericDocument(Name=self.Name, content=[heading]))
        docs.append(self.ContentFile)

        return docs


