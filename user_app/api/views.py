from user_app.api.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST',])
def register(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)


