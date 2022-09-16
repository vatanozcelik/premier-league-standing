from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json

from .models import League, Team
# Create your views here.


def home(request):
    return render(request, "core/home.html")


def premeir_league(request):
    data = Team.objects.filter(league_id=1)

    context = {
        'teams': data
    }

    return render(request, "core/premier_league.html", context)


def La_liga(request):
    la_liga = Team.objects.filter(league_id=2)
    context = {
        'teams': la_liga
    }
    return render(request, "core/la_liga.html", context)


def League_1(request):
    league_1 = Team.objects.filter(league_id=3)
    context = {
        'teams': league_1
    }
    return render(request, "core/league_1.html", context)
