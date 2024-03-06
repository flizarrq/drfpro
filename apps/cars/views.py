from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import CarFilter
from .models import CarsModel
from .serializers import CarsSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarsSerializer
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarsSerializer
