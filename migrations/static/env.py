from migrations.base_env import DatabaseInfo, run_migrations, specify  # type: ignore

import opt_public_server.static.database
from opt_public_server.main.settings import settings


specify(
    DatabaseInfo(
        url=settings.static_database_url,
        engine=opt_public_server.static.database.engine,
        metadata=opt_public_server.static.database.Base.metadata,
    )
)

run_migrations()
