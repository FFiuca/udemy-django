from rest_framework import serializers
from django.contrib.auth.models import User

class UserService:

    def register(self, obj):
        password = obj.validated_data['password']
        password2 = obj.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({
                'error': 'P1 and P2 is not same'
            })

        if User.objects.filter(email=obj.validated_data['email']).exists():
            raise serializers.ValidationError({
                'error': 'Email Already Taken!'
            })

        user = User(email=obj.validated_data['email'], username=obj.validated_data['username'], password=password)

        user.set_password(password)
        user.save()

        return user

