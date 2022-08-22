from migrations.base_env import DatabaseInfo, run_migrations, specify  # type: ignore

from opt_public_server.common.settings import get_settings
from opt_public_server.static.database import Base, engine


specify(
    DatabaseInfo(
        url=get_settings().static_database_url,
        engine=engine,
        metadata=Base.metadata,
    )
)

run_migrations()
