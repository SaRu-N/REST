
from django.contrib import admin
from django.urls import path
from func_based import views as func
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi',func.student_api,name='studentapi'),
    path('studentapi/<int:pk>/',func.student_api,name='studentapi'),
]
