from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest.views import *

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'job', JobViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

