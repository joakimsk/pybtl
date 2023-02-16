#!/usr/bin/env python

import pyseabird

def main():
    #bottlefile = pyseabird.Btl("sta0078.btl")
    my_dict = dict()
    my_dict["<hi-ship-var>"] = "R/V \"Kristine Bonnevie\""
    my_dict["<hi-station-var>"] = "9999"
    my_dict["<hi-echodepth-var>"] = "344.85"
    my_dict["<hi-log-var>"] = "7313.064"
    my_dict["<hi-wind-dir-force-var>"] = "15 12"
    my_dict["<hi-air-temp-dry-var>"] = "7.7"
    my_dict["<hi-weather-sky-var>"] = ""
    my_dict["<hi-sea-var>"] = ""
    my_dict["<hi-cruise-var>"] = "2023006003"
    my_dict["<hi-atmospheric-pressure-var>"] = "1030.9"
    pyseabird.ReplacePlaceholderVariables("sta.btl", "out.btl", my_dict, dryrun=False)

if __name__ == '__main__':
    main()