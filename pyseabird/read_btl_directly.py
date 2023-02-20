# Class for reading btl directly file format

import pandas as pd
import re

class ReadBtlDirectly:
    def __init__(self, filename):
        self.df = self.__return_data_df(BTL_FILE=filename)

    # read fixed-width column values
    def __col_values_iter(self, line, col_widths):
        i = 0
        for w in col_widths:
            start = i
            end = i + w
            yield line[start:end].lstrip()
            i += w

    def __col_values(self, line, col_widths):
        return list(self.__col_values_iter(line, col_widths))

    def __return_data_df(self, BTL_FILE): # from gist https://gist.github.com/joefutrelle/7f6e23ac7ac480a2c2b9712c12355dde
        lines = []

        with open(BTL_FILE) as fin:
            for l in fin.readlines():
                # skip header lines
                if l.startswith('#') or l.startswith('*'):
                    continue
                lines.append(l.rstrip())

        # the first line is the first line of column headers
        col_headers = re.split(r' +',lines[0])[1:]
        # third line and on are the data lines
        lines = lines[2:]

        #print(col_headers)

        # average values are every two lines
        avg_lines = lines[::2]
        # the lines with the time (and sddev values) are the ones immediately following the average value lines
        time_lines = lines[1::2]

        # columns are 11 characters wide, except the first two
        col_widths = [7,15] + [11] * (len(col_headers) - 2)

        # now assemble the rows of the dataframe
        rows = []

        for al, tl in zip(avg_lines, time_lines):
            cvs = self.__col_values(al, col_widths)
            time = self.__col_values(tl, col_widths)[1] # just use the first value
            cvs[1] = '{} {}'.format(cvs[1], time)
            rows.append(cvs)

        df = pd.DataFrame(rows, columns=col_headers)
        return df

if __name__ == "__main__":
    print("Test btl.py")
    object = ReadBtlDirectly("sta0078.btl")
    print(object.dataframe)