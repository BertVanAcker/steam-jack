from steam_jack.Documentor import Documentor,DocumentorObjects


documentor = Documentor.Documentor(DEBUG=True,LOGGER=None)


#load the steam module content
intro_file = open("input/intro.txt", "r")


#read the intro text
IntroductionText =intro_file.read()



text = "Introduction text, this can be formatted using the markdown language."

intro=DocumentorObjects.Cell(Title='Smart Farming STEAM module - Bodemvochtigheid',Text=IntroductionText,Type='markdown',Format='intro')

steam_module = DocumentorObjects.SteamModule(Name='SmartFarming_course1',Domain='SmartFarming',Introduction=intro,SupportedDevices=intro,RelatedModules=intro)
documentor.generateSTEAM_notebook(SteamObject=steam_module,output='output/')