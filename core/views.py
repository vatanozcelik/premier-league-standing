from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

from .models import League, Team
# Create your views here.

def home(request):
    teams = pd.DataFrame(list(Team.objects.all().values()))
    teams['points'] = teams['win']*3 + teams['draw']
    teams['average'] = teams['scored'] - teams['conceded']
    teams = teams.sort_values(by=['points', 'average'], ascending=False)
    # dataframe back to dictionary
    teams = teams.to_dict('dict')
    print("type of teams whether dict or not ---->>>>>>" ,type(teams))
    

    return render(request, "core/home.html", teams)