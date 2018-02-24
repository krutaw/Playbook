'''
Models.py - provides the necessary models for the application
'''

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class SME(models.Model):
    '''
    Defines the SME model
    '''
    key = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False, verbose_name=_("User name"))
    emailaddress = models.EmailField(max_length=255, null=False, verbose_name=_("Email Address"))
    phoneregex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    phonenumber = models.CharField(max_length=20, null=False, blank=False, validators=[phoneregex])
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
    '''
    Defines Team model
    '''
    key = models.AutoField(primary_key=True)
    teamname = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Team Name"))
    teammanager = models.ForeignKey(to=SME, related_name="teammgr", on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Team Manager"))
    smes = models.ManyToManyField("SME", related_name="teammembr", verbose_name=_("Team Members"))

    def __str__(self):
        return self.teamname

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')


class Calendar(models.Model):
    '''
    Calendar Model
    '''
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
    '''
    RecurRule Model
    '''
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
    '''
    Schedule Model
    '''
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
    '''
    ScheduleRotation Model
    '''
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


class Certificate(models.Model):
    '''
    Certificate Model
    '''
    key = models.AutoField(primary_key=True)
    certname = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Certificate Name"))
    certpass = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Certificate password"))
    certificate = models.CharField(max_length=2048, null=True, blank=True, verbose_name=_("Certificate"))

    def __str__(self):
        return self.certname

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')


class Actions(models.Model):
    '''
    Actions Model
    '''
    key = models.AutoField(primary_key=True)
    actionname = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Action Name"))
    actiontypechoices = (
        ("twilio_sms", "Twilio SMS"),
        ("twilio_call", "Twilio Call"),
        ("hipchat", "HipChat"),
        ("email", "Email"),
        ("ansible", "Ansible Playbook"),
        ("recovery_check", "Recovery Check"),
    )
    actiontype = models.CharField(max_length=50, choices=actiontypechoices, null=False, blank=False, verbose_name=_("Action Type"))
    assoccert = models.ForeignKey(to=Certificate, related_name="associatedcert", on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Associated Certificate"))
    actionparams = models.CharField(max_length=1024, null=True, blank=True, verbose_name=_("Action Params"))
    assocsched = models.ForeignKey(to=Schedule, related_name="associatedsched", on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Associated Schedule"))

    def __str__(self):
        return self.actionname

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Action')
        verbose_name_plural = _('Actions')


class Play(models.Model):
    '''
    Play  Model
    '''
    key = models.AutoField(primary_key=True)
    playname = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Play Name"))
    playorder = models.IntegerField(null=False, blank=False, verbose_name=_("Play Order"))
    playcommand = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Play Command"))
    retries = models.IntegerField(null=False, blank=False, verbose_name=_("Retry Count"))
    recovercommand = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Recovery Check Command"))

    def __str__(self):
        return self.playname

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Play')
        verbose_name_plural = _('Plays')
        ordering = ['playorder']


class PlayBook(models.Model):
    '''
    PlayBook Model
    '''
    key = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Playbook Name"))
    orderedplay = models.ManyToManyField("Play", related_name="play", verbose_name=_("Play Name"))

    # class Meta:
    #     '''
    #     Meta class for the model.
    #     '''
    #     ordering = ['play']
