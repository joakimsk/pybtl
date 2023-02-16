# Class for Btl file format

from .seabirdfile import SeabirdFile
from .enums import GenericStarHeader, GenericStarStarHeader

class Btl:
    def __init__(self, filename):
        # Private
        self._SeabirdFile = SeabirdFile(filename)
        self._stardict = self._SeabirdFile.return_star_dict(delim="=")
        self._starstardict = self._SeabirdFile.return_starstar_dict(delim=":")

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
                print("Key not in values, skipping", key)
        return res

    def resolve_data(self):
        print("resolve data")