from django.contrib import admin

from core.models import Footballer, League, Team

# Register your models here.

admin.site.register(Footballer)
admin.site.register(League)
admin.site.register(Team)

