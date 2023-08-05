from django.contrib.auth.models import User
from rest_framework import serializers
from user_app.api.services import UserService

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_style': 'password'}, # setting for when display generated view
        write_only=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {
                'write_only' : True # to add kwargs from User Model
            }
        }

    def save(self):
        return UserService.register(self=self,obj=self)
