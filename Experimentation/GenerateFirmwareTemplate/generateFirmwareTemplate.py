from steam_jack.Documentor import Documentor,DocumentorObjects

documentor = Documentor.Documentor(DEBUG=True,LOGGER=None)

#define firmware prototype
firmware_prototype = DocumentorObjects.FirmwarePrototype(Name='Test',Description='Auto-generated firmware template',DeviceName='Microbit')

#add function prototypes
paramter1 = DocumentorObjects.FunctionParameter(Name='Richting',Description='Richting van de lineaire beweging',datatype='enum',enumDefinition=['vooruit','achteruit'],default='vooruit')
paramter2 = DocumentorObjects.FunctionParameter(Name='Snelheid',Description='Snelheid van de lineaire beweging',datatype='int',enumDefinition=[],default=100)
func1 = DocumentorObjects.FunctionPrototype(partName='Beweeg',Description='Functie om de robot chassis een lineaire beweging te laten uitvoeren voor 1 seconde.',parameterList=[paramter1,paramter2])

firmware_prototype.FunctionPrototypes.append(func1)

documentor.generateFirmwareTemplate_python(FirmwareObject=firmware_prototype,output='output/')