from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # имя приложения
    app_name: str = "VPN Sync Service"

    # куда пинговать
    ping_url: str = "https://example.com"

    # Интервал в минутах
    ping_minutes: int = 5

    # телега
    telegram_bot_token: str | None = None
    telegram_chat_id: str | None = None

    # откуда читать переменные окружения
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()