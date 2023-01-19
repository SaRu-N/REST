from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission

# Session Authentication
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     # permission_classes =[IsAuthenticated]
#     # permission_classes =[IsAuthenticatedOrReadOnly]
#     # permission_classes =[DjangoModelPermissions]
#     permission_classes =[DjangoModelPermissionsOrAnonReadOnly]
#     # permission_classes =[IsAdminUser]

# Basic Authentication
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes =[IsAuthenticated]

# Custom Permission
class StudentViewSet(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes =[MyPermission]
