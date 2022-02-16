from steam_jack.Documentor import Documentor,DocumentorObjects

documentor = Documentor.Documentor(DEBUG=True,LOGGER=None)

text = "Introduction text, this can be formatted using the markdown language."

codeExplenation = """ this is a very
                        long code description if I had the
                        energy to type more and more ..."""

code = " print('Hello World!')\n" \
       "print('second line of code')"

textWithImage = " this is a very long code description if I had the energy to type more and more ...\n" \
                "![Example image](assets/mtiny.png)"

cell1=DocumentorObjects.Cell(Title='Markdown test',Text=text,Type='markdown',Format='intro')
cell2=DocumentorObjects.Cell(Title='Code test',Text=codeExplenation,Code=code,Type='code',Format='subsection')
notebook = DocumentorObjects.Notebook(Name='first_test',Description='No real description',content=[cell1,cell2])

documentor.generateNotebook(NotebookObject=notebook,output='output/')