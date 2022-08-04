from pydantic import BaseSettings


class Settings(BaseSettings, env_file=".env"):
    static_database_url: str


# Dismiss Pylance false positive
settings = Settings.parse_obj({})
