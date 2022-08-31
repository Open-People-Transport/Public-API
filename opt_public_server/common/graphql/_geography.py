import strawberry

from opt_public_server.common import core
from opt_public_server.common.utils import description


Latitude = strawberry.scalar(
    core.Latitude,
    description=description(core.Latitude),
    serialize="{:8.6f}".format,
    parse_literal=lambda l: core.Latitude(l.value),
)


Longitude = strawberry.scalar(
    core.Longitude,
    description=description(core.Longitude),
    serialize="{:9.6f}".format,
    parse_literal=lambda l: core.Longitude(l.value),
)


@strawberry.type(description=description(core.Geolocation))
class Geolocation:
    lat: Latitude
    lon: Longitude

    @classmethod
    def from_model(cls, model: core.Geolocation):
        return cls(
            lat=model.lat,
            lon=model.lon,
        )


@strawberry.input(description=description(core.Geolocation))
class GeolocationInput:
    lat: Latitude
    lon: Longitude

    def to_model(self) -> core.Geolocation:
        return core.Geolocation(
            lat=self.lat,
            lon=self.lon,
        )


@strawberry.type(description=description(core.Geobounds))
class Geobounds:
    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    @classmethod
    def from_model(cls, model: core.Geobounds):
        return cls(
            min_lat=model.min_lat,
            min_lon=model.min_lon,
            max_lat=model.max_lat,
            max_lon=model.max_lon,
        )


@strawberry.input(description=description(core.Geobounds))
class GeoboundsInput:
    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    def to_model(self) -> core.Geobounds:
        return core.Geobounds(
            min_lat=self.min_lat,
            min_lon=self.min_lon,
            max_lat=self.max_lat,
            max_lon=self.max_lon,
        )
