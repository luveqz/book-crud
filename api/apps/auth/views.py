from django.shortcuts import render

from rest_framework import generics

from . import models
from . import serializers

class SignUpView(generics.CreateAPIView):
    serializer_class = serializers.SignUpSerializer
