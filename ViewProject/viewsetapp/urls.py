
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router =DefaultRouter()
# Register StudentViewSet with Router
router.register('studentapi',views.StudentViewSet,basename='student')
# router.register('studentapi/<int:pk>',views.StudentViewSet,basename='student')

urlpatterns = [
   path('',include(router.urls))
]
