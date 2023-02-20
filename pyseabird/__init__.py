"""pyseabird is a python package that provides support to read Seabird Seasave files, including .btl and .cnv."""

from .seabirdfile import SeabirdFile
from .read_btl_directly import ReadBtlDirectly
from .btl import Btl
from .cnv import Cnv
from .enums import *
from .utilities import *

__version__ = "0.0.1"
