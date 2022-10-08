from core.views import home
from django.urls import path
from core.views import (
    TeamListView,
    LeagueListView,
    upload_csv,
    # players,
    # LeagueListView,
    # league_teams,
    # footballer_list,
)

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', LeagueListView.as_view(), name='league'),
    path('team/<slug:slug>/', TeamListView.as_view(), name='team'),
    # path('<slug:slug>/', league_teams, name='league'),
    # path('team/<slug:slug>/', footballer_list, name='team'),
]
