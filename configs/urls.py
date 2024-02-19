from django.urls import include, path

urlpatterns = [
    path('auto_parks', include('apps.auto_cars.urls')),
    path('cars', include('apps.cars.urls')),
]
