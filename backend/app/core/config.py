from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_title: str
    app_version: str
    frontend_origin: str


settings = Settings()  # type: ignore
