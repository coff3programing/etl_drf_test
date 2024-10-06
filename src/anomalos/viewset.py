""" Views """
from rest_framework import viewsets
from .models import AnomaliesModel, ErrorsModel
from .serializers import AnomalieSerializer, ErrorSerializers

# Create your views here.


class AnomaliesView(viewsets.ModelViewSet):
    """ CRUD Operations """
    queryset = AnomaliesModel.objects.all()
    serializer_class = AnomalieSerializer


class ErrorView(viewsets.ModelViewSet):
    """ Erros Crud """
    queryset = ErrorsModel.objects.all()
    serializer_class = ErrorSerializers
