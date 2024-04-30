# urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('image_api.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=False), name='index'),
]
