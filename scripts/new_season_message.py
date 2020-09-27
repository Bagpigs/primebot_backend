from app_prime_league.models import Team
from telegram_interface import send_message
from telegram_interface.messages import GENERAL_MATCH_LINK
from utils.constants import EMOJI_ONE, EMOJI_MINDBLOWN, EMOJI_SOON, EMOJI_ARROW, EMOJI_CLOVER, EMOJI_FIGHT


def main():
    # teams = Team.objects.exclude(telegram_id__isnull=True, division__isnull=True, id=89678)
    teams = Team.objects.filter(telegram_id__isnull=False, division__isnull=False)
    for team in teams:
        next_match = team.games_against.order_by("game_day").first()
        pattern = f"\*Das nächste Match ist natürlich gegen " \
                  f"{EMOJI_ARROW}[{next_match.enemy_team.name}]({GENERAL_MATCH_LINK}{next_match.game_id}). 😇"

        send_message(msg=pattern, chat_id=team.telegram_id)


def run():
    main()
