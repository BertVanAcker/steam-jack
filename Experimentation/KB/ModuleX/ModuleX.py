from steam_jack.KnowledgeBase.STEAMModuleConcepts import STEAMModule,ModuleContent
from steam_jack.Documentor.Documentor import Documentor

ModuleX = STEAMModule(Title="ModuleX",Description='First module',Version="0.0.1")

#add the content
introduction = ModuleContent(Name="Inleiding Module X",ContentFileReference="input/intro.md",isIntroduction=True)
opdracht1 = ModuleContent(Name="Opdracht 1",ContentFileReference="input/Opdracht1.md",isIntroduction=False)

ModuleX.Content.append(introduction)
ModuleX.Content.append(opdracht1)
ModuleX.requiredFunctions=['Function X',"Function Y"]

docs = ModuleX.documentation()

documentHandler = Documentor(DEBUG=True)
documentHandler.generateMarkdown(docList=docs,output='generated/ModuleX.md')

