from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from opt_public_server.common.settings import get_settings


engine = create_engine(get_settings().static_database_url, future=True, echo=True)
make_session = sessionmaker[Session](bind=engine, future=True)


def gen_session() -> Iterator[Session]:
    with make_session() as session:
        yield session
