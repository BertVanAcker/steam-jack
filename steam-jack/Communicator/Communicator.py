###################################################################################################
# Copyright (c) 2022, B.MKR.
#
# All rights reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###################################################################################################
#
#   @brief: Communicator class handling the generic communcation patterns
#
#   @Context: steam-jack
#
###################################################################################################

class Communicator():
    """
        Communicator: Class representing the generic communication handler

         :param bool DEBUG: setting the verbose
    """
    def __init__(self,DEBUG=True):
        self.DEBUG = DEBUG


    def genericWrite(self,id,cmd,parameterList=[]):
        """
                  Function to compose & write a steam-jack command to the communcation bus

                  :param string id: Name identifier of the targetted device
                  :param string cmd: Command identifier
                  :param list parameters: parameterList

                  :return bool writeSuccess: successfull bus write identification (-1 = error)
            """
