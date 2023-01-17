from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer

# pk not required
class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
# pk required
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


# Separate Views

# class StudentList(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView
# ):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

