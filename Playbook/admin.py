from django.contrib import admin
from .models import SME, Team, Calendar

# Register your models here.
class SMEAdmin(admin.ModelAdmin):
    list_display = ("username",)

class TeamAdmin(admin.ModelAdmin):
    list_display = ("teamname",)

class CalendarAdmin(admin.ModelAdmin):
    list_display = ("calname", "calendarteam",)


admin.site.register(SME,SMEAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Calendar,CalendarAdmin)
