
from django.contrib import admin
from django.urls import path, include
from api import views
from myapi import views as myviews
from nestedapi import views as nviews
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('singer',views.SingerViewSet,basename='singer')
router.register('song',views.SongViewSet,basename='song')
router.register('nsinger',nviews.SingerViewSet,basename='nsinger')
router.register('nsong',nviews.SongViewSet,basename='nsong')
router.register('student',myviews.StudentViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework'))
]
