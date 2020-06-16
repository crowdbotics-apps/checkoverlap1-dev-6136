from rest_framework import authentication
from users.models import Address, Bank
from .serializers import AddressSerializer, BankSerializer
from rest_framework import viewsets


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Address.objects.all()


class BankViewSet(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Bank.objects.all()
