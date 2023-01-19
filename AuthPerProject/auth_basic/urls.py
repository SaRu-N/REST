
from django.urls import path, include
from . import views

urlpatterns = [
    path('studentapi/',views.student_api,name='studentapi'),
    path('studentapi/<int:pk>/',views.student_api,name='studentapi'),
]
