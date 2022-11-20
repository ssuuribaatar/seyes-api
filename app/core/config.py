from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    LOCAL: bool = True
    APP_VERSION = "0.0.1"
    APP_NAME = "SEYES"
    API_PREFIX = "/api"

    API_KEY: str = "sample_api_key"
    IS_DEBUG: bool = False

    ICINGA_USERNAME = "root"
    ICINGA_PASSWORD = "86f524b7c36862ed"
    ICINGA_HOSTNAME = "192.168.8.196"
    ICINGA_PORT = "5665"

    class Config:
        env_file = ".env"
        case_sensitive = True
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
