from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from . mypagination import MyPagination
# Create your views here.

class StudentApi(ListAPIView):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer
    pagination_class =MyPagination
    
    
    

