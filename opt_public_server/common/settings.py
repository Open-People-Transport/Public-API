from functools import lru_cache
from typing import TYPE_CHECKING, TypeAlias

from pydantic import BaseSettings, Field


if TYPE_CHECKING:
    HttpUrl: TypeAlias = str
else:
    from pydantic import HttpUrl


class Settings(BaseSettings, env_file=".env"):
    app_title: str = "Open People Transport"
    app_description: str
    app_version: str
    app_license: str
    author_name: str
    website: HttpUrl
    static_database_url: str = Field(default=...)


@lru_cache
def get_settings() -> Settings:
    import importlib.metadata

    package, *_ = __package__.partition(".")
    metadata = importlib.metadata.metadata(package)
    return Settings(
        app_description=metadata["summary"],
        app_version=metadata["version"],
        app_license=metadata["license"],
        author_name=metadata["author"],
        website=metadata["home-page"],
    )
