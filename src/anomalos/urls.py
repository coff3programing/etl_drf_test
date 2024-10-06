""" URLS """
from rest_framework.routers import DefaultRouter
from .viewset import AnomaliesView, ErrorView

router = DefaultRouter()

router.register('anomalies', AnomaliesView)
router.register('errors', ErrorView)

urlpatterns = router.urls
