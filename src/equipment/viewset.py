""" Viewsets for equipment app """
from rest_framework import viewsets
from .models import VariablesModels, EquipmentModel
from .serializers import VariablesSerializer, EquipmentSerializer

# Create your views here.


class VariablesViewSet(viewsets.ModelViewSet):
    """ Variables Viewset """
    queryset = VariablesModels.objects.all()
    serializer_class = VariablesSerializer


class EquipmentsViewSet(viewsets.ModelViewSet):
    """ Equipments Viewset """
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentSerializer
