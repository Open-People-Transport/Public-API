import strawberry

from opt_public_server.common.models.geography import (
    Geobounds as GeoboundsModel,
    Geolocation as GeolocationModel,
    Latitude as LatitudeModel,
    Longitude as LongitudeModel,
)
from opt_public_server.common.utils import description


Latitude = strawberry.scalar(
    LatitudeModel,
    description=description(LatitudeModel),
    serialize="{:8.6f}".format,
    parse_literal=lambda l: LatitudeModel(l.value),
)


Longitude = strawberry.scalar(
    LongitudeModel,
    description=description(LongitudeModel),
    serialize="{:9.6f}".format,
    parse_literal=lambda l: LongitudeModel(l.value),
)


@strawberry.type(description=description(GeolocationModel))
class Geolocation:
    lat: Latitude
    lon: Longitude

    @classmethod
    def from_model(cls, model: GeolocationModel):
        return cls(
            lat=model.lat,
            lon=model.lon,
        )


@strawberry.input(description=description(GeolocationModel))
class GeolocationInput:
    lat: Latitude
    lon: Longitude

    def to_model(self) -> GeolocationModel:
        return GeolocationModel(
            lat=self.lat,
            lon=self.lon,
        )


@strawberry.type(description=description(GeoboundsModel))
class Geobounds:
    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    @classmethod
    def from_model(cls, model: GeoboundsModel):
        return cls(
            min_lat=model.min_lat,
            min_lon=model.min_lon,
            max_lat=model.max_lat,
            max_lon=model.max_lon,
        )


@strawberry.input(description=description(GeoboundsModel))
class GeoboundsInput:
    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    def to_model(self) -> GeoboundsModel:
        return GeoboundsModel(
            min_lat=self.min_lat,
            min_lon=self.min_lon,
            max_lat=self.max_lat,
            max_lon=self.max_lon,
        )
