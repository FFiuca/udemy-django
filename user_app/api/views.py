from user_app.api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.throttling import AnonRateThrottle
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistedToken
from user_app import models # needed to call observer signals, HOMEWORK: find how to auto discover observer signals
from user_app.api.throttling import RegisterThrottle

# try to custom login buil-in but can't yet
@api_view(['POST',])
class CustomAuth(ObtainAuthToken):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        jwt_token = RefreshToken.for_user(user)
        jwt_token = {
            'access' : str(jwt_token.access_token),
            'refresh' : str(jwt_token)
        }

        data = {
            'code' : 200,
            'data' : {
                'token': token,
                'jwt_token': jwt_token
            }
        }

        return Response(data=data, status=data.status)
# print('custom auth', dir(CustomAuth().as_view())) # to get avaible objects list of class
obtain_auth_token2 = CustomAuth

@api_view(['POST',])
@throttle_classes([RegisterThrottle])
def register(request):

    if request.method == 'POST':
        print('masuk post')
        serializer = UserSerializer(data=request.data)

        # automatic call validation exception to return error message
        # serializer.is_valid(raise_exception=True)

        if serializer.is_valid()!=True:
            return Response(data= {
                'status':400,
                # 'data' : serializer._errors,
                'data' : serializer.errors,
            }, status=400)

        print('masuk valid')
        user = serializer.save()

        jwt_token = RefreshToken.for_user(user)
        print('jwt', jwt_token)
        jwt_token = {
            'access' : str(jwt_token.access_token),
            'refresh' : str(jwt_token),
        }

        return Response(data={
            'status' : 201,
            'data': {
                **serializer.data,
                'token' : Token.objects.get(user=user).key,
                'jwt_token' : jwt_token
            }
        }, status=200)

@api_view(['POST','GET',])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method in ['POST', 'GET']:
        delete = request.user.auth_token.delete()

        return Response(data={
            'status':200,
        }, status=status.HTTP_200_OK)
