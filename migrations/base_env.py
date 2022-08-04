import logging
from dataclasses import dataclass
from logging.config import fileConfig

from alembic import context
from sqlalchemy import Engine, MetaData


config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")


@dataclass
class DatabaseInfo:
    url: str
    engine: Engine
    metadata: MetaData


db: DatabaseInfo = None  # type: ignore[assignment]


def specify(info: DatabaseInfo):
    global db
    db = info


def run_migrations_offline() -> None:
    context.configure(
        url=db.url,
        target_metadata=db.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    with db.engine.connect() as connection:
        context.configure(connection=connection, target_metadata=db.metadata)
        with context.begin_transaction():
            context.run_migrations()


def run_migrations() -> None:
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()
