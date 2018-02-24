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
    username = serializers.CharField(required=True, allow_null=True)
    emailaddress = serializers.CharField(required=True, allow_null=True)
    phonenumber = serializers.CharField(required=True, allow_null=True)
    givenname = serializers.CharField(required=True, allow_null=True)
    surname = serializers.CharField(required=True, allow_null=True)

    class Meta:
        '''
        Meta class for the serializer.
        '''
        model = SME
        fields = '__all__'
