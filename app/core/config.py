from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Task Management API"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./task_manager.db"
    secret_key: str = "change-this-secret-key-before-production"
    access_token_expire_minutes: int = 60
    algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
