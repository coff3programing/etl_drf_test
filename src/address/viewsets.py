""" Viewsets for address app """
from rest_framework import viewsets
from .models import AddressModel, TeamsModels
from .serializers import AddressSerializer, TeamsSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """ Viewset for address app """
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer


class TeamsViewSet(viewsets.ModelViewSet):
    """ Viewset for teams app """
    queryset = TeamsModels.objects.all()
    serializer_class = TeamsSerializer
