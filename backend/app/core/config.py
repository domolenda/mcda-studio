from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str
    app_version: str
    frontend_origin: str

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
