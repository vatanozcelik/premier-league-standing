from django.contrib import admin

from core.models import Footballer, League, Team


class TeamAdmin(admin.ModelAdmin):
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


admin.site.register(Footballer)
admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
