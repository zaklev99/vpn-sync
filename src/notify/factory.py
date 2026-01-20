from config import settings
from notify.telegram import TelegramNotifier


def build_notifier() -> TelegramNotifier | None:
    if settings.telegram_bot_token and settings.telegram_chat_id:
        return TelegramNotifier(
            bot_token=settings.telegram_bot_token,
            chat_id=settings.telegram_chat_id,
        )
    return None
