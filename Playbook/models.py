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
    teammanager = models.ForeignKey(to=Team, related_name="calendarteam", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Team Name"))



    def __str__(self):
        return self.calname

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Calendar')
       	verbose_name_plural = _('Calendars')
