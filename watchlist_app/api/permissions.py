from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) or request.method=='GET')

class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS :
            # do logic for method GET, HEAD, OPTIONS
            return True
        else:
            # do logic for DDM permission
            print('logic DDL permission', obj.user, obj)

            return obj.user == request.user
