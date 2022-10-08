from django.contrib.auth.decorators import permission_required
from django.contrib import messages
import io
import csv
from django.shortcuts import render, get_object_or_404
import pandas as pd
import json
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


class LeagueListView(ListView):
    model = Team
    template_name = 'core/league.html'
    context_object_name = 'teams'
    paginate_by = 10

    def get_queryset(self):
        league = get_object_or_404(League, slug=self.kwargs['slug'])
        return Team.objects.filter(league_id=league.id)


class TeamListView(ListView):
    model = Footballer
    template_name = 'core/team.html'
    context_object_name = 'footballers'
    paginate_by = 10

    def get_queryset(self):
        team = get_object_or_404(Team, slug=self.kwargs['slug'])
        return Footballer.objects.filter(team_id=team.id)


#  f u n c t i o n   b a s e d  v i e w

"""

def league_teams(request, slug):
    league = get_object_or_404(League, slug=slug)
    teams = Team.objects.filter(league_id=league.id)

    context = {
        'teams': teams,
    }
    return render(request, "core/league.html", context)


def footballer_list(request, slug):
    team = get_object_or_404(Team, slug=slug)
    footballers = Footballer.objects.filter(team_id=team.id)

    context = {

        'footballers': footballers,
    }
    return render(request, "core/team.html", context)
"""


@permission_required('admin.can_add_log_entry')
def upload_csv(request):

    template = "core/upload_csv.html"

    prompt = {
        'order': 'order should player position and team'
    }
    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not csv file')

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)  # most csv file has header

    Footballer.objects.all().delete()
    League.objects.all().delete()
    Team.objects.all().delete()

    for col in csv.reader(io_string, delimiter=';', quotechar='|'):

        league, _ = League.objects.get_or_create(name=col[5])

        team, _ = Team.objects.get_or_create(
            name=col[4],
            league=league
        )

        footballer = Footballer(
            player=col[1],
            position=col[3],
            team=team
        )
        footballer.save()

    context = {}

    return render(request, template, context)
