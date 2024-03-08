from django.urls import path

from .views import UserCreateView, UserAddAvatarView, UserToAdminView, AdminToUserView, UserBlockView, UserUnblockView

urlpatterns = [
    path('', UserCreateView.as_view(), name='create_user'),
    path('/avatar', UserAddAvatarView.as_view(), name='user_avatar'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='block_user'),
    path('/<int:pk>/unblock', UserUnblockView.as_view(), name='use_unblock')
]
