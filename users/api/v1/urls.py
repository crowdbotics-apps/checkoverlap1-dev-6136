from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AddressViewSet, BankViewSet

router = DefaultRouter()
router.register("address", AddressViewSet)
router.register("bank", BankViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
