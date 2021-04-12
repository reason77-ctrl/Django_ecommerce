from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"   #['url', 'username', 'email', 'is_staff']

