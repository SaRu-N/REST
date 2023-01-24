from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class StudentApi(ListAPIView):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(enrolled_by=user)

