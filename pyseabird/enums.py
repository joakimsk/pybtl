# Enums

from enum import Enum

class GenericHashHeaderCnv(Enum):
    NQUAN = "nquan"
    NVALUES = "nvalues"
    UNITS = "units"
    NAME = "name" # array of all elements
    SPAN = "span" # array of all elements and span of data
    INTERVAL = "interval"
    START_TIME = "start_time"
    BAD_FLAG = "bad_flag"


class GenericStarHeader(Enum):
    FILENAME = "FileName"
    SW_VERSION = "Software Version"
    TEMP_1_SN = "Temperature SN"
    COND_1_SN = "Conductivity SN"
    #TEMP_2_SN = "Temperature SN" ?
    #COND_2_SN = "Conductivity SN" ?
    SYS_UPLOAD_TIME = "System UpLoad Time"
    NMEA_LAT = "NMEA Latitude"
    NMEA_LON = "NMEA Longitude"
    NMEA_UTC_TIME = "NMEA UTC (Time)"

class GenericStarStarHeader(Enum):
    SHIP = "Ship"
    STATION = "Station"
    ECHO_DEPTH = "Echodepth"
    LOG = "Log"
    WIND_DIR_FORCE = "Wind-Dir/Force"
    AIR_TEMP_DRY = "Air-temp (dry)"
    WEATHER_SKY = "Weather Sky"
    SEA_STATE = "Sea"
    CRUISE_NUMBER = "Cruise"
    PLATFORM_NUMBER = "Platform no"
    SEABIRD_932_SN = "STB 9/32 sn"
    ATMOSPHERIC_PRESSURE = "Atmospheric pressure"
