from django.contrib import admin
from django.urls import path, include

import app

urlpatterns = [
    path('', include('rest.urls')),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('mobile_app.urls'))
]
