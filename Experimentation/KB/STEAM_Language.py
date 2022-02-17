from steam_jack.KnowledgeBase.STEAMLanguageConcepts import STEAMLanguage,LanguageConcept,LanguageElement,AbstractFunction,UserInterface,functionParameter,BlockExample
from steam_jack.Documentor.Documentor import Documentor
#in this file, the chassis kinematic language elements are defined and linked to the steam language


def Lineair_movement_language():

    #-----------------------------------------------------------------------------------------------------------------
    #                                   Define language element
    #-----------------------------------------------------------------------------------------------------------------
    Lineair_Movement = LanguageElement(Name="Beweging_lineair", Description="Lineaire beweging van het robot chassis.")

    # -----------------------------------------------------------------------------------------------------------------
    #                                   Define language function - ENTRY
    # -----------------------------------------------------------------------------------------------------------------
    example1 = BlockExample(Title="Voorbeeld 1: Lineaire beweging vooruit", Description="In dit voorbeeld wordt eerst de robot geinitialiseerd en daarna 10 keer een vooruit beweging uitgevoerd.",BlockCodeReference="C:/Users/B.MKR/Documents/03_Repositories/steam-jack/Resources/Assets/SteamLanguage/Robotics/Chassis_Kinematics/Lineair_Movement/examples/Lineair_Movement_Entry_Forward.PNG")
    example2 = BlockExample(Title="Voorbeeld 1: Lineaire beweging achteruit", Description="In dit voorbeeld wordt eerst de robot geinitialiseerd en daarna 10 keer een achteruit beweging uitgevoerd.",BlockCodeReference="C:/Users/B.MKR/Documents/03_Repositories/steam-jack/Resources/Assets/SteamLanguage/Robotics/Chassis_Kinematics/Lineair_Movement/examples/Lineair_Movement_Entry_Backward.PNG")

    # define the userinterface with correct paramters
    direction = functionParameter(Name="Beweging", Description="Deze parameter definieert de richting van de lineaire beweging. De richting kan vooruit of achteruit zijn.",Datatype="Enum")
    Lineair_Movement_Entry_UI = UserInterface(isImplemented=True, Formalism="blockcode",
                                              BlockIcon="C:/Users/B.MKR/Documents/03_Repositories/steam-jack/Resources/Assets/SteamLanguage/Robotics/Chassis_Kinematics/Lineair_Movement/Lineair_Movement_Entry.PNG",
                                              ExtensionID="sj_robotica_arduino;sj_robotica_cyberpi;sj_robotica_microbit",
                                              ExtensionCategory="Robotica - Basis", FunctionParameters=[direction],UI_Examples=[example1,example2])

    # define entry-level abstract function
    Lineair_Movement_Entry = AbstractFunction(Name="Beweging_lineair_Entry",
                                              Description="Start een lineaire beweging van je robot. De beweging blijft 1 seconde actief en voert de beweging uit op halve snelheid, dit uit veiligheidsoverwegingen.",
                                              Complexity="entry", FunctionType="COMMAND",
                                              UserInterface=Lineair_Movement_Entry_UI)

    Lineair_Movement.AbstractFunctions.append(Lineair_Movement_Entry)

    # -----------------------------------------------------------------------------------------------------------------
    #                                   Define language function - INTERMEDIATE
    # -----------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------------
    #                                   Define language function - ADVANCED
    # -----------------------------------------------------------------------------------------------------------------

    return Lineair_Movement


#define the complete STEAM language
STEAMLanguage = STEAMLanguage(Name="BMKR_STEAM_LANGUAGE",Description="The B.MKR STEAM language for education",Version="0.0.1")

#define a language concept
Kinematica_chassis = LanguageConcept(Name="Kinematica_chassis",Description="Kinematica functies van een robot chassis.",Domain="Robotics",DEBUG=True)

#define language elements
Lineair_Movement = Lineair_movement_language()

#add language elements to language concept
Kinematica_chassis.LanguageElements.append(Lineair_Movement)

#add language concept to STEAM language
STEAMLanguage.LanguageConcepts.append(Kinematica_chassis)
x=1

#------------------------------------------------------------------
#           FETCH THE DOCUMENTATION
#------------------------------------------------------------------

docs = Lineair_Movement.documentation()

#------------------------------------------------------------------
#           GENERATE WORD DOCX
#------------------------------------------------------------------
documentHandler = Documentor(DEBUG=True)
documentHandler.generateDocx(docList=docs,output='generated/LineaireBeweging.docx')
documentHandler.generateMarkdown(docList=docs,output='generated/LineaireBeweging.md')
x=1