from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from football.models import Games
from football.models import Teams
# Create your views here.

def league_table(request):
    html = '<ul>'
    a = Teams.objects.all()
    for i in a:
        html += "<li> {id}; {name}; {points} </li>" .format(id=i.id, name=i.name, points=i.points)
    html +='</ul>'
    return HttpResponse(html)

def games_played(request):
    b = Games.objects.all()
    c = Teams.objects.get(id=id)
    html ='<html>'
    html +='<head>'
    html +='<link rel="stylesheet" href="...." type="text/css" media="screen">'
    html +='</head>'
    html +='<body>'
    html += '<ul>'
    for y in b:
        html += "<li> {team_home}; {team_away}; Wynik {team_home_goals}:{team_away_goals}" .format(team_home=y.team_home, team_away=y.team_away, team_home_goals=y.team_home_goals, team_away_goals=y.team_away_goals)
    html +='</ul>'
    html +='</body>'
    html +='</html>'
    return HttpResponse(html)


    """
    html = ''
    team=Teams.objects.get(id=16)
    dane = Games.objects.filter(team_home=team).filter(team_away=team)
    html =''
    for el in dane:
        html += '{id}</br>' .format(id=el.id)
    html += dane
    return HttpResponse(html)
    """