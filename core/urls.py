from core.views import (
    home,
    # fixtures,
    team_info,
    League_1,
    La_liga,
    premeir_league,
)
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('la-liga-standing/', La_liga, name='la-liga'),
    path('league-1-standing/', League_1, name='league-1'),
    path('premier-league-standing/', premeir_league, name='premier-league'),
    path('footballer/', team_info, name='footballer'),
    # path('fixtures/', fixtures, name='fixtures'),

]
