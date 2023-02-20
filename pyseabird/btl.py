# Class for Btl file format

from pyseabird.seabirdfile import SeabirdFile
from pyseabird.enums import GenericStarHeader, GenericStarStarHeader
import pandas as pd
import re

class Btl:
    def __init__(self, filename):
        # Private
        self._SeabirdFile = SeabirdFile(filename)
        self._stardict = self._SeabirdFile.return_star_dict(delim="=")
        self._starstardict = self._SeabirdFile.return_starstar_dict(delim=":")
        self._datalines = self._SeabirdFile.return_datalines()
        self._hash_xml = self._SeabirdFile.return_hash_xml()

        # Public
        self.star_header = self.__filter_dictionary(self._stardict,  GenericStarHeader)
        self.starstar_header = self.__filter_dictionary(self._starstardict,  GenericStarStarHeader)

    def __filter_dictionary(self, dictionary, filter_enum):
        valid_keys = [member.value for member in filter_enum]
        res = dict()
        for key, value in dictionary.items():
            if key in valid_keys:
                res[key] = value
            else:
                pass
               #print("Key not in values, skipping", key)
        return res

    def return_data_df(self): # from gist https://gist.github.com/joefutrelle/7f6e23ac7ac480a2c2b9712c12355dde
        lines = []

        for line in self._datalines:
            # skip header lines
            if line.startswith('#') or line.startswith('*'):
                continue
            lines.append(line.rstrip())

        print(self._datalines)

        # the first line is the first line of column headers
        col_headers = re.split(r' +',lines[0])[1:]
        # third line and on are the data lines
        lines = lines[2:]

        #print(col_headers)

        # average values are every four lines
        avg_lines = lines[::4]
        # the lines with the time (and sddev values) are the ones immediately following the average value lines
        time_lines = lines[1::4]

        # columns are 11 characters wide, except the first two
        col_widths = [7,15] + [11] * (len(col_headers) - 2)

        # read fixed-width column values
        def col_values_iter(line, col_widths):
            i = 0
            for w in col_widths:
                start = i
                end = i + w
                yield line[start:end].lstrip()
                i += w

        def col_values(line, col_widths):
            return list(col_values_iter(line, col_widths))

        # now assemble the rows of the dataframe
        rows = []

        for al, tl in zip(avg_lines, time_lines):
            cvs = col_values(al, col_widths)
            time = col_values(tl, col_widths)[1] # just use the first value
            cvs[1] = '{} {}'.format(cvs[1], time)
            rows.append(cvs)

        df = pd.DataFrame(rows, columns=col_headers)
        return df

    def return_xml(self):
        return self._hash_xml

if __name__ == "__main__":
    print("Test btl.py")