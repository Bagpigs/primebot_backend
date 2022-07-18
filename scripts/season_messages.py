from app_prime_league.models import Team
from bots.message_dispatcher import MessageDispatcher
from bots.messages import NotificationToTeamMessage

season_end_message = """
Hallo {team.name}, 

die Gruppenphase des aktuellen PrimeLeague-Splits ist vorbei und damit geht der Primebot bis zum nächsten Split in eine kurze Pause.

Wenn ihr uns noch kein Feedback gegeben habt, würden wir uns darüber freuen, sodass wir den Primebot weiter verbessern können.
🔥 [Link zum Feedback](https://feedback.primebot.me/) 🔥


Sternige Grüße
Grayknife und Orbis
"""

season_start_message = """
Hallo {team.name}, 

die Anmeldung für den [Winter Split 2022](https://www.primeleague.gg/de/leagues/prm/2126-summer-split-2021) hat begonnen, also let´s go!
Mit dem PrimeBot startet ihr perfekt in den kommenden Split, ohne dass ihr jemals wieder etwas verpasst. 😱

Sternige Grüße
Grayknife und Orbis

"""

message = """
Hallo {team.name},

einige haben es gefordert, viele haben es sich gewünscht: der PrimeBot ist jetzt OpenSource. Wenn ihr Ideen zu Features habt, 
neue Features implementieren wollt oder Bugs beheben möchtet, findet ihr alles weitere dazu auf [GitHub](https://github.com/random-rip/primebot_backend). Auch wenn ihr keine Programmierer:innen seid, wir sammeln auch Feedback zu Features die in der Pipeline sind. 
Schaut also gerne bei den Issues vorbei, die mit "Teamfeedback needed" getaggt sind!

**Werbung** Partnerschaft mit singularIT
<MAX>

Sternige Grüße
Grayknife, Orbis & Mörlin
"""


def main():
    teams = Team.objects.get_registered_teams().filter()
    for team in teams:
        try:
            print(team)
            dispatcher = MessageDispatcher(team)
            msg = NotificationToTeamMessage(team=team, custom_message=message)
            dispatcher.dispatch_raw_message(msg=msg)
        except Exception as e:
            print(e)


def run():
    main()
