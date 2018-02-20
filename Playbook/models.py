from django.db import models
from django.core.validators import RegexValidator
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from django.utils.translation import ugettext_lazy as _

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class SME(models.Model):
    key = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False, verbose_name=_("User name"))
    emailaddress = models.EmailField(max_length=255, null=False, verbose_name=_("Email Address"))
    phoneregex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    phonenumber = models.CharField(max_length=20, null=False,blank=False,validators=[phoneregex])
    givenname = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Subject Matter Expert')
       	verbose_name_plural = _('Subject Matter Experts')

class Team(models.Model):
    key = models.AutoField(primary_key=True)
    teamname = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Team Name"))
    teammanager = models.ForeignKey(to=SME, related_name="teammgr", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Team Manager"))
    smes = models.ManyToManyField("SME", related_name="teammembr",verbose_name=_("Team Members"))

    def __str__(self):
        return self.teamname

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Team')
       	verbose_name_plural = _('Teams')

class Calendar(models.Model):
    key = models.AutoField(primary_key=True)
    calname = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Calendar Name"))
    calendarteam = models.ForeignKey(to=Team, related_name="calendarteam", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Team Name"))

    def __str__(self):
        return self.calname

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Calendar')
       	verbose_name_plural = _('Calendars')


class RecurRule(models.Model):
    key = models.AutoField(primary_key=True)
    rulename = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Rule Name"))
    ruledesc = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Rule Description"))
    rulefreq = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Rule Frequency"))
    ruleparams = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Rule Parameters"))

    def __str__(self):
        return self.rulename

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Recurrence Rule')
       	verbose_name_plural = _('Recurrence Rules')

class Schedule(models.Model):
    key = models.AutoField(primary_key=True)
    schedulename = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Schedule Name"))
    schedulecalendar = models.ForeignKey(to=Calendar, related_name="schedcal", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Schedule Calendar"))

    def __str__(self):
        return self.schedulename

    class Meta:
        '''
        Meta class for the model. 
        '''
        verbose_name = _('Schedule')
       	verbose_name_plural = _('Schedules')


class ScheduleRotation(models.Model):
    key = models.AutoField(primary_key=True)
    oncall = models.ForeignKey(to=SME, related_name="oncall", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("OnCall Admin"))
    order = models.IntegerField(null=False, blank=False, verbose_name=_("Oncall Order"))
    oncallschedule = models.ForeignKey(to=Schedule, related_name="oncallschedule", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("OnCall Schedule"))

    def __str__(self):
        return self.oncallschedule.schedulename

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Schedule Order')
       	verbose_name_plural = _('Schedule Orders')
