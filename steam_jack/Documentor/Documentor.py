###################################################################################
#	Author:			Bert Van Acker (bva.bmkr@gmail.com)
#	Version:		0.1.0
#	Lisence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#
#	Description:	Documentor class handling document and template generation
###################################################################################

#imports
import nbformat as nbf
from os import mkdir
from os.path import exists, dirname, join
import jinja2

class Documentor():
    """
        Documentor: Class representing the generic documentation handler

         :param bool DEBUG: setting the verbose
         :param object Logger: Logger object for uniform logging
    """
    def __init__(self,DEBUG=True,LOGGER=None):

        #verbose and logging
        self.DEBUG = DEBUG
        self.LOGGER = LOGGER


    def generateNotebook(self,NotebookObject,output):
        """
                Function to generate a jupyter notebook

                 :param object NotebookObject: Jupyter notebook class
                 :param string output: Path to the output location
            """

        self.notebook = nbf.v4.new_notebook()

        content = []
        for cell in NotebookObject.Content:
            title = '#'+cell.Title   #heading 1 title
            text = cell.Text
            if cell.Type=='markdown':
                content.append(nbf.v4.new_markdown_cell(title+text))
            if cell.Type == 'code':
                content.append(nbf.v4.new_code_cell(title + text))

        #add all cells to the notebook
        self.notebook['cells'] = content

        #Generate the jupyter notebook and store in output
        fname = output+NotebookObject.Name+'.ipynb'
        with open(fname, 'w') as f:
            nbf.write(self.notebook, f)


    def generateFirmwareTemplate_python(self,FirmwareObject,output):

        # Create the output folder
        srcgen_folder = join(output, 'Generated')
        if not exists(srcgen_folder):
            mkdir(srcgen_folder)

        # Initialize the template engine.
        jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('/Users/bertvanacker/Documents/BertVanAcker/03_RemoteRepositories/steam-jack/steam_jack/'),
            trim_blocks=True,
            lstrip_blocks=True)

        # Load the Java template
        template = jinja_env.get_template('Documentor/templates/Firmware_Python_DeviceFunctions.template')

        # Generate  device-specific part of python firmware prototype

        with open((join(srcgen_folder, 'DeviceSpecific.py')), 'w') as f:
            f.write(template.render(object=FirmwareObject))


