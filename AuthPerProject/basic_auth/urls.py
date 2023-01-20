
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . auth import CustomAuthToken
# Creating Router Object
router =DefaultRouter()
# Register StudentViewSet with Router
router.register('studentapi',views.StudentViewSet,basename='student')


urlpatterns = [
   path('',include(router.urls)),
   # path('gettoken/',obtain_auth_token),
    # path('gettoken/', CustomAuthToken.as_view())
]
