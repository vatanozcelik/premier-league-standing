from django.contrib import admin

from core.models import Footballer, League, Team


class FootballerAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'team'
    )
    search_fields = (
        'team',
        'player'
    )


class TeamAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = (
        'name',
        'league',
    )
    list_filter = (
        'league',
    )
    prepopulated_fields = {"slug": ("name",)}


class LeagueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Footballer, FootballerAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
