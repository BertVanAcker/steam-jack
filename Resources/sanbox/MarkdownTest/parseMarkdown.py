import marko
from steam_jack.Documentor import DocumentorObjects

from marko.renderer import Renderer


class CustomRenderer(Renderer):
    """The most common renderer for markdown parser"""

    def render_markdown2GenericDocument(self,document):

        contentList = []
        #read the markdown file
        textFile = open(document, "r")
        parsed = marko.parse(textFile.read())
        for child in parsed.children:
            if 'Heading' in str(type(child)):
                content = self.render_heading(child)
                contentList.append(content)
            if 'Paragraph' in str(type(child)):
                content = self.render_paragraph(child)
                contentList.append(content)

        # setup a generic document
        return DocumentorObjects.GenericDocument(Name='test',content=contentList)


    def render_paragraph(self, element):

        paragraph = ""
        for child in element.children:
            if 'LineBreak' in str(type(child)):
                paragraph= paragraph+ "\n"
            else:
                paragraph = paragraph + child.children

        return DocumentorObjects.Paragraph(Text=paragraph)

    def render_heading(self, element):
        return DocumentorObjects.Header(Text=element.children[0].children ,Level=element.level) #only supporting single-line headers





customRenderer = CustomRenderer()
genericDocument = customRenderer.render_markdown2GenericDocument(document="input/TEST.md")
a = 1