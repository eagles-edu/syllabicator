import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret-key")
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "5000"))
    debug: bool = os.getenv("FLASK_ENV", "development") == "development"


settings = Config()
