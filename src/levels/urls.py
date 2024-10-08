""" Address URL Configuration """
# from rest_framework.routers import DefaultRouter
from django.urls import path
from .viewsets import LevelsViewSet
from .views import UploadLevelsView


urlpatterns = [
    path('', UploadLevelsView.as_view()),
    path('<int:pk>/', LevelsViewSet.as_view()),
]
