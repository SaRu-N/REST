
from django.contrib import admin
from django.urls import path, include
from api import views
from myapi import views as myviews
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('singer',views.SingerViewSet,basename='singer')
router.register('song',views.SongViewSet,basename='song')
router.register('student',myviews.StudentViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework'))
]
