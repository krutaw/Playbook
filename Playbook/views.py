from django.shortcuts import render
from rest_framework import viewsets

class SMEViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SMEs to be viewed or edited.
    """
    queryset = SME.objects.all()
    serializer_class = SMESerializer
