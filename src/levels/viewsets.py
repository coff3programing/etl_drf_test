""" API Viewsets """
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import LevelsModel
from .serializers import LevelsSerializer

# Create your views here.


class LevelsViewSet(RetrieveUpdateDestroyAPIView):
    """ Detail patient queryset. """
    allowed_methods = ["GET", "PUT", "DELETE"]
    queryset = LevelsModel.objects.all()
    serializer_class = LevelsSerializer
