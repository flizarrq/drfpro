from django.urls import include, path

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('auto_parks', include('apps.auto_cars.urls')),
    path('cars', include('apps.cars.urls')),
    path('users', include('apps.users.urls'))
]
