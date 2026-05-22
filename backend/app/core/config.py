from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App
    app_name: str = "SceneSwitch"
    environment: str = "development"
    debug: bool = True
    
    # API Keys
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    
    # Database
    database_url: str = ""
    
    # Redis
    redis_url: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()
