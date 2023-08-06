from user_app.api.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app import models # needed to call observer signals

@api_view(['POST',])
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

        return Response(data={
            'status' : 201,
            'data': {
                **serializer.data,
                'token' : Token.objects.get(user=user).key,
            }
        }, status=200)

