from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

# class StudentApi(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class =StudentSerializer
#     # def get_queryset(self):
#     #     user=self.request.user
#     #     return Student.objects.filter(enrolled_by=user)
#     filter_backends =[DjangoFilterBackend]
#     filterset_fields =['name','city']

# Search Filter
class StudentApi(ListAPIView):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer
    filter_backends =[SearchFilter]
    search_fields =['name','city']
    # search_fields =['^name']
    # search_fields =['=name']

class StudentApi(ListAPIView):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer
    filter_backends =[OrderingFilter]
    # ordering_fields =['name']
    # ordering_fields ='__all__'
    
    

