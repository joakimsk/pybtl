#!/usr/bin/env python

import pandas as pd
import re
import pyseabird

def main():
    psb = pyseabird.ReadBtlDirectly('sta.btl')
    df = psb.df
    print(df)

if __name__ == '__main__':
    main()