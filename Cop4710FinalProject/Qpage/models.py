from django.db import models

## Schemea Models, translated in python

class VideoGames(models.Model):
    GameName = models.CharField(max_length = 100, primary_key=True)
    Developer = models.CharField(max_length = 100)
    Rating = models.CharField(max_length = 1)

class Team(models.Model):
    TeamName = models.CharField(max_length = 100, primary_key = True)
    Wins = models.IntegerField()
    Losses = models.IntegerField()
    Draws = models.IntegerField()
    Region = models.CharField(max_length = 100)
    TotalWinnings = models.IntegerField()
    Sponsor = models.CharField(max_length = 100)

class Players(models.Model):
    TeamName = models.ForeignKey(Team, on_delete=models.CASCADE)
    GameName = models.CharField(max_length = 100)
    RealName = models.CharField(max_length = 100)
    Country = models.CharField(max_length = 100)
    Earnings = models.IntegerField()

class PlaysGame(models.Model):
    GameName = models.ForeignKey(VideoGames, on_delete=models.CASCADE)
    PlayerID = models.ForeignKey(Players, on_delete=models.CASCADE)

class Tournaments(models.Model):
    TournamentName = models.CharField(max_length = 100, primary_key = True)
    Year = models.DateTimeField('Start Date')
    Location = models.CharField(max_length = 100)
    PrizeMoney = models.IntegerField()
    Winner = models.CharField(max_length = 100)

class Match(models.Model):
    Round = models.CharField(max_length = 100)
    Year = models.DateField()

class PlaysIn(models.Model):
    TeamName = models.ForeignKey(Team, on_delete=models.CASCADE)
    MatchID = models.ForeignKey(Match, on_delete=models.CASCADE)
