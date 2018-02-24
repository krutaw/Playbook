'''
Serializer module for the API
'''
from rest_framework import serializers
from Playbook.models import SME
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
