from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class ApplicantsSerializer(serializers.ModelSerializer):
    Job = JobSerializer()

    class Meta:
        model = Applicants
        fields = '__all__'


class CircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circular
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
