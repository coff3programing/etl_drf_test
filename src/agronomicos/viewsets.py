""" Viewsets for agronomicos app """
from rest_framework import viewsets
from .models import UploadAgronomicosFilesModel
from .serializers import UploadFileSerializer

# Create your views here.


class UploadAgronomicosFilesView(viewsets.ModelViewSet):
    """ Viewsets for agronomicos app """
    queryset = UploadAgronomicosFilesModel.objects.all()
    serializer_class = UploadFileSerializer
