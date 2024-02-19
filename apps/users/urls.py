from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateDestroyView, UsersAddAutoParkView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    path('/<int:pk>/auto_parks', UsersAddAutoParkView.as_view(), name='users_add_auto_park')
]