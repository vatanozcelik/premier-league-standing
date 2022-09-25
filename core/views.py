from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import pandas as pd
import json
import requests
from django.views.generic import (
    # DetailView,
    ListView,
)


from .models import League, Team, Footballer


"""
to type of ordering 
1- beanth of corresponding model
class Meta:
    ordering = ('-point', '-average')

2- at the end of query as below
.order_by('-point', '-average')
"""

"""
        C L A S S    B A S E D    V I E W
"""

# class LeagueListView(ListView):
#     model = Team
#     template_name = "league.html"
#     context_object_name = "teams"

#     def get_context_data(self, **kwargs):
#         context = super(LeagueListView, self).get_context_data(**kwargs)
#         league = get_object_or_404(League, slug=kwargs.get('slug'))
#         context['teams'] = Team.objects.filter(league_id=league.id)
#         return context


def home(request):
    return render(request, "core/home.html")


def league_teams(request, slug):
    league = get_object_or_404(League, slug=slug)
    teams = Team.objects.filter(league_id=league.id)

    context = {
        'teams': teams,
        'footballer': Footballer.objects.all(),
    }
    return render(request, "core/league.html", context)


def footballer_list(request, slug):
    team = get_object_or_404(Team, slug=slug)
    footballers = Footballer.objects.filter(team_id=team.id)

    context = {

        'footballers': footballers,
    }
    return render(request, "core/team.html", context)
