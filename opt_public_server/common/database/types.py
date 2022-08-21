import uuid
from decimal import Decimal
from typing import Annotated, get_args

from sqlalchemy.orm import mapped_column
from sqlalchemy.types import Numeric, String, TypeEngine, Uuid


UUIDPK = Annotated[uuid.UUID, mapped_column(Uuid, primary_key=True)]
FullName = Annotated[str, 60]
Abbreviation = Annotated[str, 12]
Latitude = Annotated[Decimal, 8, 6]
Longitude = Annotated[Decimal, 9, 6]

type_annotation_map: dict[type, TypeEngine] = {
    FullName: String(*get_args(FullName)[1:]),
    Abbreviation: String(*get_args(Abbreviation)[1:]),
    Latitude: Numeric(*get_args(Latitude)[1:]),
    Longitude: Numeric(*get_args(Longitude)[1:]),
}
