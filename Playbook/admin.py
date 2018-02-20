from django.contrib import admin
from .models import SME

# Register your models here.
class SMEAdmin(admin.ModelAdmin):
    list_display = ("user_name")

admin.site.register(SME,SMEAdmin)
