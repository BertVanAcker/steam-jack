import json
import os
import subprocess


code = """\
from datetime import datetime
print(datetime.now().strftime("%A"))
print("Hello World")
"""

def create_message(msg_type, msg_data=None, msg_process=""):
    return json.dumps({"type": msg_type, "data": msg_data, "process": msg_process})

start_cmd = create_message("start", {"sourceScript": code})
print(start_cmd)



