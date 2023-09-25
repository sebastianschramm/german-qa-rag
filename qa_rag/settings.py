from pydantic import BaseSettings


class Settings(BaseSettings):
    serper_api_key: str
    openai_api_key: str
    openai_model: str


settings = Settings()
