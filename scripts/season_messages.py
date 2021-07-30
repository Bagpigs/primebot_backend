from app_prime_league.models import Team
from communication_interfaces.message_dispatcher import MessageDispatcher


def main():
    teams = Team.objects.get_watched_team_of_current_split()
    pattern = """
Hallo {team.name}, 

die Gruppenphase des aktuellen PrimeLeague-Splits ist vorbei und damit geht der Primebot bis zum nächsten Split in eine kurze Pause.
Die Tiebreaker und Playoff-Spiele, die diese Woche noch stattfinden, werden von unserem Bot (noch) *nicht* berücksichtigt.

Sternige Grüße
Grayknife und Orbis
"""
    for team in teams:
        try:
            print(team)
            dispatcher = MessageDispatcher(team)
            msg = pattern.format(team=team, )
            dispatcher.dispatch_raw_message(msg=msg)
        except Exception as e:
            print("ERROR", e)


# python manage.py runscript debug
def run():
    main()
