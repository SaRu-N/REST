
from django.contrib import admin
from django.urls import path
from func_based import views as func
from class_based import views as cl
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',func.student_api,name='studentapi'),
    path('studentapi/<int:pk>/',func.student_api,name='studentapi'),
    path('studentapicl/',cl.StudentApi.as_view(),name='studentapicl'),
    path('studentapicl/<int:pk>/',cl.StudentApi.as_view(),name='studentapicl'),
]
