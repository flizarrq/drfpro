from django.urls import path
from cars.views import CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('cars', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='car_retrieve_update_delete'),
]
