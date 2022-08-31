from pydantic import ConstrainedDecimal, ConstrainedStr


class FullName(ConstrainedStr):
    min_length = 4
    max_length = 60


class Abbreviation(ConstrainedStr):
    min_length = 2
    max_length = 12


class Latitude(ConstrainedDecimal):
    """
    Latitude in decimal format with 6 places after the floating point.

    Ranges from -90.000000 to 90.000000.

    Provides precision of about 10cm.
    """

    ge = -90
    le = 90
    max_digits = 8
    decimal_places = 6


class Longitude(ConstrainedDecimal):
    """
    Longitude in decimal format with 6 places after the floating point.

    Ranges from -180.000000 to 180.000000.

    Provides precision of about 10cm.
    """

    ge = -180
    le = 180
    max_digits = 9
    decimal_places = 6
