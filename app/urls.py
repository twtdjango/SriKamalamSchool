from django.conf.urls.static import static
from django.urls import path

from KamalamSchool import settings
from app.views import *

urlpatterns = [
    path('', home, name='Home'),
    path('about', about, name='About'),
    # path('/teachers', teachers, name='teachers'),
    # path('/classes', classes, name='classes'),
    # path('/blog', blog, name='blog'),
    path('contactus', contactus, name='ContactUs'),
    path('application', application, name='Application'),
    path('image_gallery', image_gallery, name='ImageGallery'),
    path('video_gallery', video_gallery, name='VideoGallery'),
    path('teachers', teachers, name='Teachers'),
    # path('/about', about, name='About'),
    # path('/about', about, name='About'),
    # path('/about', about, name='About'),
    # path('/about', about, name='About'),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
