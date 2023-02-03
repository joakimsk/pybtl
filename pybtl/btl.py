# Class for Btl file format

class Btl:
    def __init__(self, filename):
        self._filename = filename
        self._starstarlines = []
        self._starlines = []
        self._hashlines = []
        self._datalines = []
        self._parse()

    def _parse(self):
        f = open(self._filename, "rt", newline='\n') # Windows newlines are \r\n 0x0D 0x0A, Linux is only \n 0x0A
        for line in f:
            clean_line = line.strip()
            if clean_line.startswith('**'):
                self._starstarlines.append(clean_line)
            elif clean_line.startswith('*'):
                self._starlines.append(clean_line)
            elif clean_line.startswith('#'):
                self._hashlines.append(clean_line)
            else:
                self._datalines.append(clean_line)

    def print_datalines(self):
        for line in self._datalines:
            print(line)