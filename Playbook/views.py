from rest_framework import viewsets
from Playbook.models import SME
from Playbook.serializers import SMESerializer


class SMEViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SMEs to be viewed or edited.
    """
    queryset = SME.objects.all()
    serializer_class = SMESerializer
