import uuid
from typing import Annotated

from sqlalchemy.orm import mapped_column
from sqlalchemy.types import Numeric, String, TypeEngine, Uuid

from opt_public_server.common.core import Abbreviation, FullName, Latitude, Longitude


UUIDPK = Annotated[uuid.UUID, mapped_column(Uuid, primary_key=True)]

type_annotation_map: dict[type, TypeEngine] = {
    FullName: String(FullName.max_length),
    Abbreviation: String(Abbreviation.max_length),
    Latitude: Numeric(Latitude.max_digits, Latitude.decimal_places),
    Longitude: Numeric(Longitude.max_digits, Longitude.decimal_places),
}
