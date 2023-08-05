from rest_framework import permissions
from watchlist_app.models import WatchList, Review

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) or request.method=='GET')

class OnlyOneTimeInputReview(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        print('check duplicate', request.method)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.method=='POST':
                check = Review.objects.filter(user=request.user).exists()
                print('check duplicate2', request.method, check)

                return check==False
            # else:
            #     return False

# need check due always passed otherwise return false
class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print('check duplicate3', request.method)
        if request.method in permissions.SAFE_METHODS :
            # do logic for method GET, HEAD, OPTIONS
            return True
        else:
            # do logic for DDM permission
            if request.method=='PUT':
                print('logic DDM permission')
                print(obj)
                print(view)

                # return True
                return obj.user == request.user
            elif request.method=='POST':
                check = Review.objects.filter(user=request.user).exists()
                print('check duplicate2', request.method, check)

                return check==False
