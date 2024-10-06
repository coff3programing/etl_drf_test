""" URLS """
from rest_framework.routers import DefaultRouter
from .viewset import EquipmentsViewSet, VariablesViewSet

router = DefaultRouter()

router.register('equipments', EquipmentsViewSet)
router.register('variables', VariablesViewSet)

urlpatterns = router.urls
