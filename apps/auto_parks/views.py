from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.cars.serializers import CarsSerializer

from .models import AutoParksModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParksModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        car_serializer = CarsSerializer(data=data)
        car_serializer.is_valid(raise_exception=True)
        car_serializer.save(auto_park=auto_park)
        serializer = AutoParkSerializer(auto_park)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = CarsSerializer(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
