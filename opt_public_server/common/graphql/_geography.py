import strawberry

from opt_public_server.common import models
from opt_public_server.common.utils import description


Latitude = strawberry.scalar(
    models.Latitude,
    description=description(models.Latitude),
    serialize="{:8.6f}".format,
    parse_literal=lambda l: models.Latitude(l.value),
)


Longitude = strawberry.scalar(
    models.Longitude,
    description=description(models.Longitude),
    serialize="{:9.6f}".format,
    parse_literal=lambda l: models.Longitude(l.value),
)


@strawberry.type(description=description(models.Geolocation))
class Geolocation:
    lat: Latitude
    lon: Longitude

    @classmethod
    def from_model(cls, model: models.Geolocation):
        return cls(
            lat=model.lat,
            lon=model.lon,
        )


@strawberry.input(description=description(models.Geolocation))
class GeolocationInput:
    lat: Latitude
    lon: Longitude

    def to_model(self) -> models.Geolocation:
        return models.Geolocation(
            lat=self.lat,
            lon=self.lon,
        )


@strawberry.type(description=description(models.Geobounds))
class Geobounds:
    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    @classmethod
    def from_model(cls, model: models.Geobounds):
        return cls(
            min_lat=model.min_lat,
            min_lon=model.min_lon,
            max_lat=model.max_lat,
            max_lon=model.max_lon,
        )


@strawberry.input(description=description(models.Geobounds))
class GeoboundsInput:
    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    def to_model(self) -> models.Geobounds:
        return models.Geobounds(
            min_lat=self.min_lat,
            min_lon=self.min_lon,
            max_lat=self.max_lat,
            max_lon=self.max_lon,
        )
