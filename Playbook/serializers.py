'''
Serializer module for the API
'''
from rest_framework import serializers
from Playbook.models import SME, Team, Calendar, Schedule, ScheduleRotation, Actions, Play, PlayBook
# added the models below because I'm lazy but have them commented out for now to allow linter to pass
# , Team, Calendar, Schedule, RecurRule, ScheduleRotation
# from Playbook.models import Certificate, Actions, Play, PlayBook


class SMESerializer(serializers.ModelSerializer):
    '''
    SME Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = SME
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    '''
    Team Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = Team
        fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):
    '''
    Calendar Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = Calendar
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    '''
    Schedule Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = Schedule
        fields = '__all__'


class ScheduleRotationSerializer(serializers.ModelSerializer):
    '''
    ScheduleRotation Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = ScheduleRotation
        fields = '__all__'


class ActionsSerializer(serializers.ModelSerializer):
    '''
    Actions Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = Actions
        fields = '__all__'


class PlaySerializer(serializers.ModelSerializer):
    '''
    Play Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = Play
        fields = '__all__'


class PlayBookSerializer(serializers.ModelSerializer):
    '''
    PlayBook Serializer
    '''
    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = PlayBook
        fields = '__all__'
