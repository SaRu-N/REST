
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('studentapi/',views.LCStudentAPI.as_view(),name='lcstudentapi'),
     path('studentapi/<int:pk>/',views.RUDStudentAPI.as_view(),name='rudstudentapi'),

    #  path('studentapi/',views.StudentList.as_view(),name='studentapi'),
    # path('studentapi/',views.StudentCreate.as_view(),name='studentapi'),
    # path('studentapi/<int:pk>/',views.StudentRetrieve.as_view(),name='studentapicl'),
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view(),name='studentapicl'),
    # path('studentapi/<int:pk>/',views.StudentDestroy.as_view(),name='studentapicl'),
]