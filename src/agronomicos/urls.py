""" URLS """
from rest_framework.routers import DefaultRouter
from .viewsets import UploadAgronomicosFilesView

router = DefaultRouter()

router.register('', UploadAgronomicosFilesView)

urlpatterns = router.urls
