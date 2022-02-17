###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Custom Markdown parser
###################################################################################
import marko
from marko.renderer import Renderer
from bs4 import BeautifulSoup

from steam_jack.Documentor import DocumentorObjects



class CustomMarkdownParser(Renderer):
    """
        CustomMarkdownParser: Class representing a custom markdown parser, overwriting the standard Renderer
    """

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
            if 'FencedCode' in str(type(child)):
                content = self.render_code(child)
                contentList.append(content)
            if 'HTMLBlock' in str(type(child)):
                content = self.render_image(child)
                contentList.append(content)
            if 'List' in str(type(child)):
                content = self.render_list(child)
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

    def render_image(self,element):
        parsed_html = BeautifulSoup(element.children)
        source = parsed_html.img['src']
        width = parsed_html.img['width']
        height = parsed_html.img['height']
        return DocumentorObjects.Image(AltText="alt",ImagePath=source,Width=width,Height=height)

    def render_code(self,element):
        return DocumentorObjects.CodeSection(Formalism=element.lang,Code=element.children[0].children)

    def render_list(self,element):
        bullet = element.bullet
        listElements = []
        for child in element.children:
            listElements.append(child.children[0].children[0].children)
        return DocumentorObjects.ListSection(Bullet=bullet,ListElements=listElements)