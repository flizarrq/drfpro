from django.urls import path

from .views import CarListCreateView, CarRetrieveUpdateDestroyView, CarAddPhotoView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='create_cars'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_cars'),
    path('/<int:pk>/photo', CarAddPhotoView.as_view(), name='cars_photo')
]
