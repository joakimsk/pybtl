# Class for CnvColumnHeaderList

import re

class CnvColumHeader:
    def __init__(self, short_name, verbose_name, residual_unit, unit_only, span_start, span_end):
        self._short_name = short_name
        self._verbose_name = verbose_name
        self._residual_unit = residual_unit
        self._unit_only = unit_only
        self._span_start = span_start
        self._span_end = span_end
        
    def __str__(self):
        return f"CnvColumn:{self._short_name}, verbose_name:{self._verbose_name} , unit:{self._unit_only}, residual_unit: {self._residual_unit}, span:{self._span_start}<->{self._span_end}"


class CnvColumnHeaderList():
    def __init__(self, name_dict, span_dict):
        self.column_headers = []

        if len(name_dict) != len(span_dict):
            Exception("SensorList: Length of name_dict and span_dict are not the same. We assume we have span for all values.")

        length_of_sensor_list = len(name_dict)

        list_of_name_dict = list(name_dict.keys()) # not really needed, contains name 0 etc
        list_of_name_values = list(name_dict.values()) # contains short_name, verbose_name and optionally unit

        list_of_span_dict = list(span_dict.keys()) # not really needed, contains span 0 etc
        list_of_span_values = list(span_dict.values()) # contains span_start and span_end values

        #print(list_of_name_values)

        for idx in range(length_of_sensor_list):
            short_name, residual_name = list_of_name_values[idx].split(':', 1) # Will only act on first :

            regexp = "\[.+\]" # should match any unit with brackets

            unit_only = None
            verbose_name = None
            residual_unit = None

            retval = re.search(regexp, residual_name)
            if retval: # we found a unit, remove it in order to shape the verbose_name
                unit_only = retval.group()
                start_of_unit = retval.start()
                verbose_name = residual_name[:start_of_unit].strip() # strip lead and tail whitespace
                residual_unit = residual_name[start_of_unit:]
               # print(unit, "started ", start_of_unit)
            else:
                verbose_name = residual_name

            span_start, span_end = list_of_span_values[idx].split(',')
            self.column_headers.append(CnvColumHeader(short_name, verbose_name, residual_unit, unit_only, span_start.strip(), span_end.strip()))


        #print(name_dict)
        #print(span_dict)