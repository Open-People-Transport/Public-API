from pydantic import BaseModel, ConstrainedDecimal, validator


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


class Geolocation(BaseModel):
    """
    Single geographical point.
    """

    lat: Latitude
    lon: Longitude


class Geobounds(BaseModel):
    """
    Rectangular geographical bounds.
    """

    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    @validator("max_lat")
    def check_max_lat_is_max(cls, max_lat, values):
        if max_lat < values["min_lat"]:
            raise ValueError("Maximum latitude has to be greater than the minimum")
        return max_lat

    @validator("max_lon")
    def check_max_lon_is_max(cls, max_lon, values):
        if max_lon < values["min_lon"]:
            raise ValueError("Maximum longitude has to be greater than the minimum")
        return max_lon
