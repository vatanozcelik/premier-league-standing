from core.views import home
from django.urls import path
from core.views import (
    # LeagueListView,
    league_teams,
    footballer_list,
    # players,
)

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', league_teams, name='league'),
    path('team/<slug:slug>/', footballer_list, name='team'),

]
