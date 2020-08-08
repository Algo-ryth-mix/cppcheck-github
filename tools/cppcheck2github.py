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


report = ET.fromstring(output)
for error in report[1]:

    log = github_log();

    if error.tag == "error":
        if error.attrib['severity']=="error":
            log.type = "failure"
        else:
            log.type = "warning"

        log.message = error.attrib['msg']

        if len(error.getchildren()) > 0:
            if error[0].tag == "location":
                log.line = error[0].attrib['line']
                log.col = error[0].attrib['column']
                log.file = error[0].attrib['file']

        else:
            log.col = "0"
            log.line = "0"
            log.file = "[Internal]"

    log.generate()
