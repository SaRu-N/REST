
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/',include('basic_auth.urls')),
    path('auth/',include('auth_basic.urls'))
]
