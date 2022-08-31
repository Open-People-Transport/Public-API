from enum import Enum


class Type(str, Enum):
    Bus = "BUS"
    Trolley = "TROLLEY"
    Tram = "TRAM"
    Minibus = "MINIBUS"
