from django.contrib import admin
from .models import SME, Team

# Register your models here.
class SMEAdmin(admin.ModelAdmin):
    list_display = ("username")

class TeamAdmin(admin.ModelAdmin):
    list_display = ("teamname")



admin.site.register(SME)
admin.site.register(Team)
