from rest_framework.permissions import BasePermission
from core.dataclasses.user_dataclass import UserDataClass


class IsAdminOrWriteOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user: UserDataClass = request.user
        if request.method == 'POST':
            return True or user.is_staff
        return user.is_staff
