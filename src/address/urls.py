""" Address URL Configuration """
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import AddressViewSet, TeamsViewSet
from .views import UpladExcelView

router = DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'teams', TeamsViewSet)

URL: str = "address"

urlpatterns = [
    path('', include(router.urls)),
    path(f'{URL}/upload_excel/', UpladExcelView.as_view()),
    path(f'{URL}/parroquia/<str:parroquia_name>', UpladExcelView.as_view())
]
