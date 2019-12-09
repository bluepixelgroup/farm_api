from rest_framework import viewsets
from farm.models import Person, Fieldman, Farmer, PersonFamily
from farm.serializers import (
    PersonSerializer, FielmanSerializer, FarmerSerializer,
    PersonFamilySerializer
)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class FielmanViewSet(viewsets.ModelViewSet):
    queryset = Fieldman.objects.all()
    serializer_class = FielmanSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = PersonFamily.objects.all()
    serializer_class = PersonFamilySerializer