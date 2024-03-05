from django.urls import path

from .views import AutoParkAddCarView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='create_auto_park'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='add_car_to_auto_park')
]
