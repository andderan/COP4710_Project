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

class Match(models.model):
    StartTime = models.DateTimeField('Start Time')
    TeamName = models.CharField(max_length = 100)
    Year = models.DateField()
class

class Team(models.model):
    TeamName = models.CharField(max_length = 100, primary_key = True)
    Country = models.CharField(max_length = 100)
    WinningsPercent = models.FloatField()
    Wins = models.IntegarField()
    Losses = models.IntegarField()

class PlaysIn(models.model):
    TeamName = ForeignKey(Team, on_delete=models.CASCADE)
    MatchID = ForeignKey(Match, on_delete=models.CASCADE)
