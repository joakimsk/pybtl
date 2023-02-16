# Class for Cnv file format

from .seabirdfile import SeabirdFile
from .enums import GenericStarHeader, GenericStarStarHeader, GenericHashHeaderCnv
from .cnvcolumns import CnvColumnHeaderList

import re

class Cnv:
    def __init__(self, filename):
        # Private
        self._SeabirdFile = SeabirdFile(filename)
        self._stardict = self._SeabirdFile.return_star_dict(delim="=")
        self._starstardict = self._SeabirdFile.return_starstar_dict(delim=":")
        self._hashdict = self._SeabirdFile.return_hash_dict(delim="=")

        # Public
        self.star_header = self.__filter_dictionary(self._stardict,  GenericStarHeader)
        self.starstar_header = self.__filter_dictionary(self._starstardict,  GenericStarStarHeader)

        # This is inefficient, we could probably push and pop instead of running data through twice
        self.hash_header = self.__filter_dictionary(self._hashdict,  GenericHashHeaderCnv)

        # Sensors
        self.hash_name_dict = self.__filter_dictionary_regexp(self._hashdict,  "name")
        self.hash_span_dict = self.__filter_dictionary_regexp(self._hashdict,  "span")
        self.column_header_list = CnvColumnHeaderList(self.hash_name_dict, self.hash_span_dict)

    def __filter_dictionary(self, dictionary, filter_enum):
        valid_keys = [member.value for member in filter_enum] # lists are not as efficient as sets or dicts
        res = dict()
        for key, value in dictionary.items(): # this is an exact match, but we have name 0 etc
            if key in valid_keys:
                res[key] = value
            else:
                pass
                #print("Key not in values, skipping", key)
        return res

    def __filter_dictionary_regexp(self, dictionary, regexp):
        res = dict()

        for key, value in dictionary.items():
            if re.match(regexp, key):
                res[key] = value
            else:
                pass
                #print("Key not in values, skipping", key)
        return res

    def resolve_data(self):
        print("resolve data")



