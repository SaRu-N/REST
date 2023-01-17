
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),

    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
 ]