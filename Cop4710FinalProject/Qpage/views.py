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

# Homepage
def home(request):
    return render(request, 'Qpage/dota.html')

# Views for Team Info
def Teams(request):
    Team_List = Team.objects.order_by('TeamName')
    context = {'Team_List': Team_List}
    return render(request, 'Qpage/team_list.html', context)

def TeamDisplay(request, Team_Int_Key):
    Team_List = Team.objects.all()
    for teams in Team_List:
        if teams.TotalWinnings == Team_Int_Key:
            Team_Name = teams.TeamName
    SelectedPlayers = SelectPlayerQuery(Team_Name)
    context = {'SelectedPlayers' : SelectedPlayers}
    return render(request, 'Qpage/team_list.html', context)

#Views for Match information

def Matches(request):
    Match_List = Match.objects.order_by('Year')
    context = {'Match_List': Match_List}
    return render(request, 'HTML', context)

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
    return render(request, 'HTML', context)
