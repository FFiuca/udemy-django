from rest_framework import serializers
from django.contrib.auth.models import User

class UserService:

    def __init__(self, outerObj):
        self.obj = outerObj

        print('self obj', self.obj)

    def register(self):
        password = self.obj.validated_data['password']
        password2 = self.obj.validated_data['password2']
        print('cek')
        if password!=password2:
            raise serializers.ValidationError({
                'error': 'P1 and P2 is not same'
            })

        if User.objects.filter(email=self.obj.validated_data['email']).exists():
            raise serializers.ValidationError({
                'error': 'Email Already Taken!'
            })

        user = User(email=self.obj.validated_data['email'], username=self.obj.validated_data['username'], password=password)

        user.set_password(password)
        user.save()

        return user

    @classmethod
    def register2(cls, data):
        # data = clss.obj # in case if you want call method without passing self param in caller method
        pass

    @staticmethod
    def register3(data):
        # in case if you want call method without passing self param in caller method but you can't accesss self instance
        pass
