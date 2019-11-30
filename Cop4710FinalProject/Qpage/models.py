from django.db import models

## Schemea Models, translated in python

class VideoGames(models.model):
    GameName = models.CharField(max_length = 100, primary_key=True)
    Developer = models.CharField(max_length = 100)
    Rating = models.CharField(max_length = 1)

class Players(models.model):
    TeamName = models.ForeignKey(Team, on_delete=models.CASCADE)
    Sponsor = models.CharField(max_length = 100)
    PlayerName = models.CharField(max_length = 100)
    Keyboard = models.CharField(max_length = 100)
    Mouse = models.CharField(max_length = 100)
    Headset = models.CharField(max_length = 100)

class PlaysGame(models.model):
    GameName = models.ForeignKey(VideoGames)
    PlayerID = models.ForeignKey(Players)

class Tournaments(models.model):
    TournamentName = models.CharField(max_length = 100, primary_key = True)
    Year = models.DateTimeField('Start Date')
    Location = models.CharField(max_length = 100)
    PrizeMoney = models.IntegarField()
    Winner = models.CharField(max_length = 100)


Match(
	MatchID: Int
	StartTime: Time
	T_name: String
	Year: Data
)

E-SportsTeam(
	TeamName: String
	Country: String
	Winnings: Float
	Wins: Int
	Losses: Int
)

PlaysIn(
	TeamName: String FORGIEN KEY
	MatchID: Int FORIEGN KEY
)
