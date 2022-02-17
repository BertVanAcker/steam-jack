###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Knowledge base class representing the steam-jack knowledge base
###################################################################################

#imports

class KnowledgeBase():
    """
        Documentor: Class representing the generic documentation handler

         :param string Name: Name of the KB_Instance
         :param string Version: Version of the KB_Instance
         :param bool DEBUG: setting the verbose

    """
    def __init__(self,Name="",Version="0.0.1",DEBUG=True):

        #verbose and logging
        self.DEBUG = DEBUG
        self.Name = Name
        self.Version = Version
