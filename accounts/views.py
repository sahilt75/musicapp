from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

from .serializers import RegisterUserSerializer, LoginSerializer


class RegisterView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(username=serializer.data['username'])
            except User.DoesNotExist:
                return Response({'status':404,'message':'User not found'})
            if not user.check_password(serializer.data['password']):
                return Response({'status':400,'message':'Invalid password'})

            return Response({'status': 200, 'message': 'Login successful'})

        else:
            return Response(serializer.errors)

