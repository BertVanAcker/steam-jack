from steam_jack.Documentor import Documentor,DocumentorObjects

documentor = Documentor.Documentor(DEBUG=True,LOGGER=None)

text = "Introduction text, this can be formatted using the markdown language."

code = "print('Hello World!')"

cell1=DocumentorObjects.Cell(Title='Markdown test',Text=text,Type='markdown')
cell2=DocumentorObjects.Cell(Title='Code test',Text=code,Type='code')
notebook = DocumentorObjects.Notebook(Name='first_test',Description='No real description',content=[cell1,cell2])

documentor.generateNotebook(NotebookObject=notebook,output='output/')