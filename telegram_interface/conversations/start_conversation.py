from telegram import Update, ParseMode
from telegram.ext import CallbackContext, ConversationHandler

from app_prime_league.models import Team
from app_prime_league.teams import register_team
from telegram_interface.commands.single_commands import set_photo
from telegram_interface.keyboards import boolean_keyboard
from telegram_interface.messages import START_GROUP, START_CHAT, TEAM_EXISTING, TEAM_ID_VALID, REGISTRATION_FINISH, \
    WAIT_A_MOMENT_TEXT, TEAM_ID_NOT_VALID_TEXT, SET_PHOTO_TEXT, \
    PHOTO_SUCESS_TEXT, PHOTO_RETRY_TEXT, CHAT_EXISTING
from utils.messages_logger import log_command, log_callbacks


# /start
@log_command
def start(update: Update, context: CallbackContext):
    chat_type = update.message.chat.type
    chat_id = update.message.chat.id
    if chat_type in ["group", "supergroup"]:
        chat_existing = Team.objects.filter(telegram_channel_id=chat_id).exists()
        if not chat_existing:
            update.message.reply_markdown(START_GROUP, parse_mode="Markdown", disable_web_page_preview=True)
            return 1
        update.message.reply_markdown(CHAT_EXISTING, parse_mode="Markdown", disable_web_page_preview=True)
        return ConversationHandler.END
    else:
        update.message.reply_markdown(START_CHAT, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return ConversationHandler.END


@log_command
def team_registration(update: Update, context: CallbackContext):
    response = update.message.text
    try:
        team_id = int(response)
    except Exception as e:
        try:
            team_id = int(response.split("/teams/")[-1].split("-")[0])
        except Exception as e:
            update.message.reply_markdown(
                TEAM_ID_NOT_VALID_TEXT,
            )
            return 1

    tg_group_id = update.message.chat.id
    context.bot.send_message(
        text=WAIT_A_MOMENT_TEXT,
        chat_id=tg_group_id,
        parse_mode=ParseMode.MARKDOWN,
    )
    team = register_team(team_id=team_id, tg_group_id=tg_group_id)
    if team is None:
        update.message.reply_markdown(
            TEAM_EXISTING,
            disable_web_page_preview=True,
        )
        return 1
    else:
        update.message.reply_markdown(
            SET_PHOTO_TEXT,
            reply_markup=boolean_keyboard(0),
        )
        return ConversationHandler.END


@log_callbacks
def set_optional_photo(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    url = Team.objects.get(telegram_channel_id=chat_id).logo_url
    successful = set_photo(chat_id, context, url)
    if successful:
        finish_registration(update, context)
    else:
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=PHOTO_RETRY_TEXT,
            reply_markup=boolean_keyboard(0),
            parse_mode=ParseMode.MARKDOWN,
        )


@log_callbacks
def finish_registration(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    team = Team.objects.get(telegram_channel_id=chat_id)
    context.bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=PHOTO_SUCESS_TEXT,
        reply_markup=None,
        parse_mode=ParseMode.MARKDOWN,

    )

    context.bot.send_message(
        text=f"{TEAM_ID_VALID}*{team.name}*\n{REGISTRATION_FINISH}",
        chat_id=chat_id,
        disable_web_page_preview=True,
        parse_mode=ParseMode.MARKDOWN,
    )
