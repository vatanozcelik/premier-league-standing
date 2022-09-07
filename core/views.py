from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json

from .models import League, Team
# Create your views here.

def home(request):
    teams = pd.DataFrame(list(Team.objects.all().values()) )
    teams['points'] = teams['win']*3 + teams['draw']
    teams['average'] = teams['scored'] - teams['conceded']
    teams = teams.sort_values(by=['points', 'average'], ascending=False)
    # dataframe back to dictionary
    json_records = teams.reset_index().to_json(orient = 'records')
    data = [] 
    data = json.loads(json_records)
    context = {
        'teams': data
    }
    print(type(context))
    print(context)

    return render(request, "core/home.html", context)