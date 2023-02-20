# Class for generic Seabird file

import xml.dom.minidom

class SeabirdFile:
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

    def return_hash_xml(self):
        my_xml_lines = ""
        for item in self._hashlines:
            if item.startswith("#"):
                clean_line = item.replace("#", "").strip()
                if clean_line.startswith("<"):
                    my_xml_lines += clean_line + "\n"
        
        dom = xml.dom.minidom.parseString(my_xml_lines)
        return dom

    def return_star_dict(self, delim="="):
        res = dict()
        for item in self._starlines:
            try:
                key, value = item.split(delim,1)
                res[key.replace("*", "").strip()] = value.strip()
            except ValueError:
                #print("return_star_dict skipping line, no delim found", item)
                continue
        return res

    def return_starstar_dict(self, delim=":"):
        res = dict()
        for item in self._starstarlines:
            try:
                key, value = item.split(delim,1)
                res[key.replace("*", "").strip()] = value.strip()
            except ValueError:
                #print("return_starstar_dict skipping line, no delim found")
                continue
        return res

    def return_hash_dict(self, delim="="):
        res = dict()
        for item in self._hashlines:
            try:
                key, value = item.split(delim,1)
                res[key.replace("#", "").strip()] = value.strip()
            except ValueError:
                #print("return_star_dict skipping line, no delim found", item)
                continue
        return res

    def return_datalines(self):
        return self._datalines
    
    def print_starlines(self):
        for line in self._starlines:
            print(line)

    def print_starstarlines(self):
        for line in self._starstarlines:
            print(line)

    def return_starstarlines(self):
        return self._starstarlines
    
    def print_hashlines(self):
        for line in self._hashlines:
            print(line)