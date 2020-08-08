import sys
import xml.etree.ElementTree as ET
from pprint import pprint

output = ""

try:
    for line in sys.stdin:
        output += line
except KeyboardInterrupt:
    sys.stdout.flush()
    pass

return_code = 0

class github_log:
    def __init__(self):
        self.type = ""
        self.file = ""
        self.line = ""
        self.col = ""
        self.message = ""

    def generate(self):
        if(self.type != ""):
            print(f"::{self.type} file={self.file},line={self.line},col={self.col}::{self.message}")
            global return_code
            return_code = 1


report = ET.fromstring(output)
for error in report[1]:

    log = github_log();

    if error.tag == "error":
        log.type = error.attrib['severity']

        log.message = error.attrib['msg']

        if len(list(error)) > 0:
            if error[0].tag == "location":
                log.line = error[0].attrib['line']
                if 'column' in error[0].attrib:
                    log.col = error[0].attrib['column']
                log.file = error[0].attrib['file']

        else:
            log.col = "0"
            log.line = "0"
            log.file = "[Internal]"

    log.generate()

sys.exit(return_code)