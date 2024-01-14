from .models import User, Data
from .serializers import UserSerializer, DataSerializer

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.http import Http404

from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User

import re

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        # Get the 'email' parameter from the request
        email = self.request.query_params.get('email', None)
        password = self.request.query_params.get('password', None)

        # Validate the email format using a simple regular expression
        if email and not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            # Handle the error for an invalid email format
            raise Http404("Invalid email format")

        # If 'email' parameter is present, use the filter method of Django ORM
        if email:
            users = User.objects.filter(email=email, password=password)

            if not users.exists():
                raise Http404("User not found")
            
            return users
            
            # # If 'password' parameter is present, check if it matches the stored password
            # if password:
            #     users = [user for user in users if check_password(password, user.password)]
            #     if not users:
            #         raise Http404("Incorrect password")
            
            # return users

        # If there is no 'email' parameter, return all users
        return User.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'User deactivated'}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.status = False
        instance.save()
    
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DataSerializer