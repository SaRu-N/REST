from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Basic Authentication
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[IsAuthenticated]
#     # permission_classes =[IsAdminUser]

# Session Authentication
class StudentViewSet(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes =[IsAuthenticated]