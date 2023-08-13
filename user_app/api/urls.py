from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user_app.api.throttling import LoginThrottle

from user_app.api.views import register, logout, obtain_auth_token2


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('login2/', obtain_auth_token2, name='login2'),
    path('logout/', logout, name='register'),

    path('register/', register, name='register'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
