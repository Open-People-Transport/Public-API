import inflection
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, declared_attr


class Base(MappedAsDataclass, DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return inflection.underscore(cls.__name__)
