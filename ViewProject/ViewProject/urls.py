
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generic/',include('genericview.urls')),
    path('concrete/',include('concreteview.urls')),
    path('viewset/',include('viewsetapp.urls')),
]
