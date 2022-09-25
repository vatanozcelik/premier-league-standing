from core.views import (
    home,
    # # fixtures,
    # team_info,
    # League_1,
    # La_liga,
    # premeir_league,
)
from django.urls import path
from core.views import (
    # LeagueListView,
    league_teams,
    footballer_list,
)

urlpatterns = [
    path('', home, name='home'),
    # path('league/<slug:slug>/', LeagueListView.as_view(), name='league'),
    path('<slug:slug>/', league_teams, name='league'),
    path('team/<slug:slug>/', footballer_list, name='team'),
    # path('fixtures/', fixtures, name='fixtures'),

]
