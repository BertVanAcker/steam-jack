import sys
import json
from io import StringIO
import contextlib

def run_py(code="print('Hello World')",VERBOSE=True):

    output=[]

    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    with stdoutIO() as s:
        exec(code)

    output.append(s)

    if VERBOSE:print(s.getvalue())
    return s.getvalue()

code = """\
from datetime import datetime
print(datetime.now().strftime("%A"))
print("Hello World")
"""

def create_message(msg_type, msg_data=None, msg_process=""):
    return json.dumps({"type": msg_type, "data": msg_data, "process": msg_process})

start_cmd = create_message("start", {"sourceScript": code})
#print(start_cmd)

output = run_py(code=code,VERBOSE=True)
print(output)