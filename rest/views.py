from rest_framework import viewsets
from rest_framework import permissions
from rest.serializers import *
from rest.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer
    # permission_classes = [permissions.IsAuthenticated]
