from django.contrib import admin
from Playbook.models import SME, Team, Calendar, RecurRule, Schedule, ScheduleRotation, Certificate, Actions, Play, PlayBook

admin.site.register(SME)
admin.site.register(Team)
admin.site.register(Calendar)
admin.site.register(RecurRule)
admin.site.register(Schedule)
admin.site.register(ScheduleRotation)
admin.site.register(Actions)
admin.site.register(Certificate)
admin.site.register(Play)
admin.site.register(PlayBook)
