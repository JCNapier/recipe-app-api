# from django.shortcuts import render

#helps create API specific view included in django rest framework
from rest_framework import generics
#must import serializer here
from user.serializers import UserSerializer 

class CreateUserView(generics.CreateAPIView):
  """Create a new user in the system"""
  #class variable that points to serializer 
  serializer_class = UserSerializer 
  


