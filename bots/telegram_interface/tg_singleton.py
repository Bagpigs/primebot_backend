import logging

import telepot
from telegram import ParseMode

from prime_league_bot import settings

bot = telepot.Bot(token=settings.TELEGRAM_BOT_KEY)

notifications_logger = logging.getLogger("notifications")


def send_message_to_devs(msg, parse_mode=ParseMode.HTML):
    try:
        send_message(msg=msg, chat_id=settings.TG_DEVELOPER_GROUP, parse_mode=parse_mode)
    except Exception as e:
        notifications_logger.exception(e)


def send_message(msg: str, chat_id: int, parse_mode=ParseMode.MARKDOWN, raise_again=False):
    """
    Sends a Message using Markdown as default.
    """
    try:
        return bot.sendMessage(chat_id=chat_id, text=msg, parse_mode=parse_mode, disable_web_page_preview=True)
    except Exception as e:
        notifications_logger.exception(
            f"Error Sending Message in Chat chat_id={chat_id} msg={msg}\n{e}")
        if raise_again:
            raise e
