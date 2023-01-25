from django.contrib import admin
from django.urls import path
from pagenumber import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentApi.as_view(),name='studentapi'),
]