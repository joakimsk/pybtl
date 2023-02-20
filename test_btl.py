import pandas as pd
import re

BTL_FILE = r'sta.btl'

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
#df.head()
print(df.iloc[0])