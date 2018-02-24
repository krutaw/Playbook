from rest_framework import viewsets
from Playbook.models import SME, Team, Calendar, Schedule, ScheduleRotation, Actions, Play, PlayBook
from Playbook.serializers import SMESerializer, TeamSerializer, CalendarSerializer, ScheduleSerializer, ScheduleRotationSerializer, ActionsSerializer, PlaySerializer, PlayBookSerializer


class SMEViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SMEs to be viewed or edited.
    """
    queryset = SME.objects.all()
    serializer_class = SMESerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Calendar to be viewed or edited.
    """
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Schedule to be viewed or edited.
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleRotationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ScheduleRotation to be viewed or edited.
    """
    queryset = ScheduleRotation.objects.all()
    serializer_class = ScheduleRotationSerializer


class ActionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Actions to be viewed or edited.
    """
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer


class PlayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Play to be viewed or edited.
    """
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class PlayBookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayBook to be viewed or edited.
    """
    queryset = PlayBook.objects.all()
    serializer_class = PlayBookSerializer
