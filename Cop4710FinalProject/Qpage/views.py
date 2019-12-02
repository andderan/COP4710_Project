from django.shortcuts import render, HttpResponse
from .models import Team, Players, Match, PlaysIn

## Selects Players given a team name
def SelectPlayerQuery(Team_Name):
    Team_List = Team.objects.order_by('TeamName')
    Players_List = Players.objects.order_by('id')
    SelectedPlayers = []
    for TeamIn in Team_List:
        for Player in Players_List:
            if TeamIn.TeamName == Player.TeamName.TeamName and TeamIn.TeamName == Team_Name:
                SelectedPlayers.append(Player)
    return SelectedPlayers
## Selects a Team given their Int Key (total winnings)
def FindTeamWithID(Team_ID):
    Team_List = Team.objects.all()
    for team in Team_List:
        if team.TotalWinnings == Team_ID:
            return team


# Homepage
def home(request):
    return render(request, 'Qpage/homepage.html')

# Views for Team Info
def Teams(request):
    Team_List = Team.objects.order_by('TeamName')
    context = {'Team_List': Team_List}
    return render(request, 'Qpage/team_list.html', context)

def TeamDisplay(request, Team_Int_Key):
    TeamSelected = FindTeamWithID(Team_Int_Key)
    SelectedPlayers = SelectPlayerQuery(TeamSelected.TeamName)
    TeamN = SelectedPlayers[0].TeamName
    context = {'SelectedPlayers' : SelectedPlayers, 'TeamN': TeamN}
    return render(request, 'Qpage/teamdata.html', context)

#Views for Match information

def Matches(request):
    Match_List = Match.objects.order_by('Year')
    PlaysIn_List = PlaysIn.objects.all()
    context = {'Match_List': Match_List, 'PlaysIn_List': PlaysIn_List}
    return render(request, 'Qpage/mathces.html', context)

def MatchDisplay(request, Match_Id):
    Match_List = Match.objects.order_by('Year')
    for MatchObject in Match_List:
        if MatchObject.id == Match_Id:
            Selected_Match = (MatchObject)
    WinningPlayers = SelectPlayerQuery(Selected_Match.Winner)
    WinningTeam = Selected_Match.Winner
    PlaysIn_List = PlaysIn.objects.order_by('TeamName')
    LosingPlayers = []
    for teams in PlaysIn_List:
        if teams.MatchID.id == Selected_Match.id and Selected_Match.Winner != teams.TeamName.TeamName:
            LosingTeam = teams.TeamName
            LosingPlayers = SelectPlayerQuery(teams.TeamName.TeamName)

    context = {'WinningPlayers': WinningPlayers, 'LosingPlayers': LosingPlayers,
              'WinningTeam': WinningTeam, 'LosingTeam': LosingTeam}
    return render(request, 'Qpage/mathces.html', context)


    # Advanced Function

def FindLoser(MatchObject):
    PlaysInList = PlaysIn.objects.all()
    for plays in PlaysInList:
        if MatchObject.id == plays.MatchID.id and MatchObject.Winner.TeamName != plays.TeamName.TeamName:
            return plays.TeamName

def FindTeamScore(TeamObject):
    PlaysInObjects = PlaysIn.objects.all()
    Matches = []
    Score = 0
    for PlayInObject in PlaysInObjects:
        if PlayInObject.TeamName.TeamName == TeamObject.TeamName:
            Matches.append(PlayInObject.MatchID)
    for match in Matches:
        if TeamObject.TeamName == match.Winner.TeamName:
            Score =  Score + (FindLoser(match).Wins / (FindLoser(match).Losses + FindLoser(match).Wins))
        else:
            Score = Score - (match.Winner.Wins / (match.Winner.Losses + match.Winner.Wins))

    return Score

def ChanceCalc(WinningScore, LossingScore):
    WinningScore = abs(WinningScore)
    LossingScore = abs(LossingScore)
    Total = WinningScore + LossingScore
    return WinningScore/Total


def Predictions(request):
    Team_List = Team.objects.order_by('TeamName')
    context = {'Team_List': Team_List}
    return render(request, 'Qpage/Predictions.html', context)

def PredictionsQue(request, TeamOneID):
    Team_List = Team.objects.all()
    context = {'Team_List': Team_List}
    return render(request, 'Qpage/PredictionsQue.html', context)

def PredictionDisplay(request, TeamOneID, TeamTwoID):
    TeamOne = FindTeamWithID(TeamOneID)
    TeamTwo = FindTeamWithID(TeamTwoID)
    TeamOneScore = FindTeamScore(TeamOne)
    TeamTwoScore = FindTeamScore(TeamTwo)
    WinningScore = 0
    LossingScore = 0
    WinningTeam = TeamOne
    LossingTeam = TeamTwo
    if TeamOneScore > TeamTwoScore:
        WinningScore = TeamOneScore
        LossingScore = TeamTwoScore
    else:
        WinningScore = TeamTwoScore
        LossingScore = TeamOneScore
        WinningTeam = TeamTwo
        LossingTeam = TeamOne

    WinnersChance = round(ChanceCalc(WinningScore, LossingScore)*100, 2)
    LossersChance = round(100 - WinnersChance, 2)
    context = {'WinnersChance': WinnersChance, 'WinningTeam': WinningTeam, 
                'LossersChance': LossersChance, 'LossingTeam': LossingTeam}
    return render(request, 'Qpage/PredictionsDisplay.html', context)



    
